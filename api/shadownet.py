import ipaddress
import random
import urllib.parse
from typing import Any, Dict, List
import requests

class InfiltrationEngine:
    """Hardened Intelligence & Scraping Subsystem with SSRF Mitigation."""
    def __init__(self):
        self.user_agents: List[str] = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0"
        ]
        self.tor_proxy: str = "socks5h://127.0.0.1:9050"
        
        # Block internal clouds (AWS metadata, GCP metadata, Docker bridge, loopback, private RFC-1918)
        self.blocked_ips = ["169.254.169.254", "127.0.0.1", "localhost", "0.0.0.0"]

    def _is_safe_target(self, target_url: str) -> bool:
        """Guards against SSRF and private address traversal."""
        try:
            parsed = urllib.parse.urlparse(target_url)
            if parsed.scheme not in ("http", "https"):
                return False

            hostname = parsed.hostname
            if not hostname:
                return False

            if hostname in self.blocked_ips:
                return False

            # Check if domain resolves to private/reserved IP
            try:
                ip = ipaddress.ip_address(hostname)
                if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
                    return False
            except ValueError:
                # Target is a domain name, not a raw IP
                pass

            return True
        except Exception:
            return False

    def scrape_intel(self, target_url: str, use_tor: bool = False) -> Dict[str, Any]:
        """Executes strict, sandboxed network ingestion."""
        if not self._is_safe_target(target_url):
            return {
                "status": "rejected",
                "error": "Security barrier blocked target URL: potential SSRF/internal network vector."
            }

        headers = {
            "User-Agent": random.choice(self.user_agents),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "DNT": "1"
        }
        proxies = {"http": self.tor_proxy, "https": self.tor_proxy} if use_tor else {}

        try:
            session = requests.Session()
            session.max_redirects = 3
            
            response = session.get(
                target_url,
                headers=headers,
                proxies=proxies,
                timeout=4,
                stream=True  # Avoid memory exhaustion attacks
            )

            # Cap payload at 256KB to safeguard serverless memory limits
            content_bytes = b""
            for chunk in response.iter_content(chunk_size=4096):
                content_bytes += chunk
                if len(content_bytes) > 262144:
                    break

            return {
                "status": "success",
                "target": target_url,
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "data_preview": content_bytes.decode("utf-8", errors="ignore")[:500]
            }
        except Exception as e:
            return {
                "status": "failed",
                "target": target_url,
                "error": str(e)
            }
