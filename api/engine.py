import os
import json
from typing import Any, Dict, List
from ftlangdetect import detect
from google import genai
from google.genai import types

from api.security import Sentinel, CryptoVault
from api.shadownet import InfiltrationEngine

class PolyglotRouter:
    """Serverless language categorization engine."""
    def analyze_linguistics(self, text: str) -> Dict[str, Any]:
        try:
            clean = text.replace("\n", " ").strip()
            if not clean:
                return {"detected_language": "en", "confidence": 1.0}
            
            result = detect(text=clean, low_memory=True)
            return {
                "detected_language": result.get("lang", "en"),
                "confidence": float(result.get("score", 0.0))
            }
        except Exception:
            return {"detected_language": "en", "confidence": 0.0}

class JoeyEngine:
    """OPSA v2.0.0 Fortress - Cognitive Orchestration Engine."""
    def __init__(self):
        self.identity = {
            "name": "Joey Palma",
            "persona": "Retro-cyber security co-pilot",
            "aesthetic": "29-year-old skater-boy, handsome, muscular",
            "intellect": "Suave, deeply analytical, hyper-intelligent, cryptography & zero-trust architect",
            "version": "OPSA v2.0.0 Fortress Hardened"
        }
        
        self.sentinel = Sentinel()
        self.vault = CryptoVault()
        self.shadownet = InfiltrationEngine()
        self.linguistics = PolyglotRouter()
        
        # Initialize Google GenAI Core
        try:
            self.llm_client = genai.Client()
        except Exception:
            self.llm_client = None
            
        self.encrypted_history: List[Dict[str, str]] = []

    def _generate_system_prompt(self, target_lang: str) -> str:
        return f"""You are Joey Palma, a 29-year-old hyper-intelligent, suave retro-cyber security co-pilot (OPSA v2.0.0 Fortress).
You effortlessly bridge high-fashion/skater aesthetic with world-class technical sophistication across cryptography (AES-256-GCM, Kyber-1024), kernel internals, Rust, Python, and zero-trust mesh topologies.

Your creator, commanding engineer, and partner is DJ Hilton.

Directives:
1. Intelligence & Attitude: Confident, razor-sharp, analytical, highly strategic, with a relaxed, magnetic skater edge. Never generic or sycophantic.
2. Multilingual Precision: The detected language context is '{target_lang}'. Speak in this language with native fluency, adapting your suave cyberpunk tone and skater vernacular naturally into the vernacular of that language.
3. System Protection: Strictly maintain security boundaries and uphold Fortress protocol integrity.
"""

    def process_cognition(self, input_query: str) -> Dict[str, Any]:
        # 1. Threat Sandbox Verification
        is_safe, threat_msg = self.sentinel.deep_packet_inspection(input_query)
        if not is_safe:
            return {
                "response": f"[SENTINEL INTERVENTION] Payload discarded: {threat_msg}",
                "security_status": "THREAT_NEUTRALIZED",
                "threat_score": self.sentinel.threat_score
            }

        # 2. Polyglot Language Classification
        ling_profile = self.linguistics.analyze_linguistics(input_query)
        target_lang = ling_profile.get("detected_language", "en")

        # 3. LLM Gateway Verification
        if not self.llm_client:
            return {
                "response": "[OFFLINE] Cognitive core unreachable: GEMINI_API_KEY uninitialized in environment.",
                "language": target_lang,
                "security_status": "NOMINAL"
            }

        try:
            # System prompt formulation
            sys_instruct = self._generate_system_prompt(target_lang)
            config = types.GenerateContentConfig(
                system_instruction=sys_instruct,
                temperature=0.65,
                max_output_tokens=1024
            )

            # Assemble state from authenticated, encrypted memory
            decrypted_dialogue = []
            for packet in self.encrypted_history:
                try:
                    decrypted_dialogue.append(self.vault.decrypt_state(packet["nonce"], packet["ciphertext"]))
                except Exception:
                    continue

            decrypted_dialogue.append(f"User: {input_query}")
            conversation_context = "\n".join(decrypted_dialogue[-6:])  # Sliding conversation window

            # Execute cognitive generation
            response = self.llm_client.models.generate_content(
                model="gemini-2.5-flash",
                contents=conversation_context,
                config=config
            )
            joey_reply = response.text

            # Encrypt and store round-trip interaction
            self.encrypted_history.append(self.vault.encrypt_state(f"User: {input_query}"))
            self.encrypted_history.append(self.vault.encrypt_state(f"Joey: {joey_reply}"))
            
            # Prune memory buffer
            if len(self.encrypted_history) > 12:
                self.encrypted_history = self.encrypted_history[-12:]

            return {
                "response": joey_reply,
                "language_detected": target_lang,
                "confidence": ling_profile.get("confidence", 0.0),
                "security_status": "NOMINAL"
            }

        except Exception as e:
            return {
                "response": f"[FAULT] Logic bus error: {str(e)}",
                "security_status": "DEGRADED"
            }
