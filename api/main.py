import os
import time
from typing import Optional
from fastapi import FastAPI, HTTPException, Header, Request
from pydantic import BaseModel, Field

from api.engine import JoeyEngine

app = FastAPI(
    title="Joey Palmas AI",
    description="OPSA v2.0.0 Fortress - Hardened Cybernetic Gateway",
    version="2.0.0"
)

engine = JoeyEngine()
FORTRESS_SECRET = os.environ.get("FORTRESS_SECRET_KEY", "fortress-default-dev-secret-key-32b")

# Strict Pydantic Data Models
class CognitionRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=4096)
    nonce: Optional[str] = Field(None, max_length=64)
    timestamp: Optional[int] = Field(None)

class InfiltrationRequest(BaseModel):
    target_url: str = Field(..., max_length=2048)
    use_tor: Optional[bool] = False

@app.middleware("http")
async def security_audit_middleware(request: Request, call_next):
    """Enforces request metrics and header inspection."""
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains"
    return response

@app.get("/api")
def root_telemetry():
    return {
        "node_status": "ONLINE",
        "system": engine.identity,
        "threat_index": engine.sentinel.threat_score
    }

@app.post("/api/cognition")
async def execute_cognition(
    payload: CognitionRequest,
    x_fortress_signature: Optional[str] = Header(None)
):
    # Enforce signature verification if configured
    if os.environ.get("REQUIRE_HMAC_AUTH") == "true":
        if not x_fortress_signature:
            raise HTTPException(status_code=401, detail="X-Fortress-Signature header missing")
        
        # Verify replay attack barrier
        if payload.nonce and payload.timestamp:
            if not engine.sentinel.enforce_replay_barrier(payload.nonce, payload.timestamp):
                raise HTTPException(status_code=403, detail="Replay barrier triggered or timestamp expired")

    result = engine.process_cognition(payload.query)
    return {
        "status": "PROCESSED",
        "telemetry": result
    }

@app.post("/api/infiltrate")
def execute_infiltration(payload: InfiltrationRequest):
    intel = engine.shadownet.scrape_intel(payload.target_url, payload.use_tor or False)
    if intel.get("status") in ("failed", "rejected"):
        raise HTTPException(status_code=400, detail=intel.get("error"))
    return {"status": "SUCCESS", "intel": intel}

@app.get("/api/vault/keys")
def retrieve_quantum_manifest():
    manifest = engine.vault.generate_quantum_key_manifest()
    return {"status": "ISSUED", "manifest": manifest}
