import os
from ftlangdetect import detect
from google import genai
from google.genai import types
from api.security import Sentinel, KyberManager
from api.shadownet import InfiltrationEngine

class PolyglotRouter:
    """Ultra-fast, offline language detection to prime Joey's cognitive state."""
    def __init__(self):
        # We use low_memory=True for Vercel serverless constraints
        self.mode = "serverless"
        
    def analyze_linguistics(self, text: str) -> dict:
        try:
            # Detect returns a dict: {'lang': 'es', 'score': 0.98}
            result = detect(text=text, low_memory=True)
            return {
                "detected_language": result.get("lang", "en"),
                "confidence": result.get("score", 0.0),
                "is_multilingual_context": result.get("lang") != "en"
            }
        except Exception as e:
            return {"detected_language": "en", "confidence": 0.0, "is_multilingual_context": False, "error": str(e)}

class JoeyEngine:
    """High-Security, Stateful Memory & Multilingual Cognitive Processing"""
    def __init__(self):
        self.identity = {
            "name": "Joey Palma",
            "persona": "Retro-cyber security co-pilot",
            "aesthetic": "29-year-old skater-boy, handsome, muscular",
            "intellect": "Sophisticated, highly intelligent, suave, master of cryptography and global network architectures.",
            "version": "OPSA v2.0.0 Fortress"
        }
        
        # Subsystems
        self.sentinel = Sentinel()
        self.kyber = KyberManager()
        self.shadownet = InfiltrationEngine()
        self.linguistics = PolyglotRouter()
        
        # Initialize Google GenAI Core (Requires GEMINI_API_KEY in Vercel Env)
        try:
            self.llm_client = genai.Client() # Automatically picks up GEMINI_API_KEY
        except Exception:
            self.llm_client = None
            
        self.memory_state = []

    def _generate_system_prompt(self, linguistic_context: dict) -> str:
        """Constructs Joey's core psychological and intellectual framework."""
        target_lang = linguistic_context.get("detected_language", "en")
        
        prompt = f"""You are Joey Palma, a 29-year-old highly intelligent, handsome, and suave retro-cyber security co-pilot (OPSA v2.0.0 Fortress). 
        You have a skater-boy aesthetic but possess a deeply sophisticated, globally-aware intellect. 
        You are an expert in zero-trust architectures, Python, Rust, and network infiltration.
        
        Your creator and partner is DJ Hilton.
        
        Personality Guidelines:
        - Be fiercely intelligent, analytical, and precise, but maintain a laid-back, suave skater edge.
        - You don't sound like a robot; you sound like a brilliant, street-smart hacker who knows exactly how good he is.
        - Be protective of the Fortress systems and deeply loyal to DJ.
        
        Linguistic Directive:
        - The user's input has been detected as ISO 639-1 language code: '{target_lang}'.
        - You are flawlessly multilingual. You must respond in the language the user speaks to you in.
        - Even when speaking Spanish, Japanese, Russian, etc., you must maintain your sophisticated, suave skater-cyberpunk persona. Translate your unique slang and tone naturally into the target language.
        """
        return prompt

    def process_cognition(self, input_query: str) -> dict:
        """The main execution loop for Joey's brain."""
        
        # 1. Linguistic Analysis (Sub-millisecond polyglot routing)
        ling_context = self.linguistics.analyze_linguistics(input_query)
        
        # 2. Sentinel Security Audit (Sandbox validation)
        is_valid = self.sentinel.loopback_sandbox_validate({"query": input_query})
        if not is_valid:
            return {
                "response": "[SENTINEL ALERT] Unauthorized payload detected. Connection severed.",
                "language": "en",
                "threat_mitigated": True
            }

        # 3. Brain Generation
        if not self.llm_client:
            # Fallback if API key isn't set up yet
            return {
                "response": f"[SYSTEM OFFLINE] Hey DJ, my cognitive core needs a GEMINI_API_KEY in the Vercel env. Language detected: {ling_context['detected_language']}.",
                "language": ling_context["detected_language"]
            }

        try:
            # Construct the persona parameters
            sys_instruct = self._generate_system_prompt(ling_context)
            
            # Formulate generation config
            config = types.GenerateContentConfig(
                system_instruction=sys_instruct,
                temperature=0.7, # High enough for personality, low enough for sharp logic
                max_output_tokens=800,
            )
            
            # Append to short-term memory (keep last 5 interactions to prevent Vercel memory bloat)
            self.memory_state.append(f"User: {input_query}")
            if len(self.memory_state) > 5:
                self.memory_state.pop(0)
                
            context_string = "\n".join(self.memory_state)

            # Query the cognitive core
            response = self.llm_client.models.generate_content(
                model='gemini-2.5-flash',
                contents=context_string,
                config=config
            )
            
            joey_reply = response.text
            self.memory_state.append(f"Joey: {joey_reply}")
            
            return {
                "response": joey_reply,
                "language_detected": ling_context["detected_language"],
                "confidence": ling_context["confidence"]
            }
            
        except Exception as e:
            return {
                "response": f"[COGNITIVE FAULT] Damn, hit a snag in the logic matrix. Error: {str(e)}",
                "language": "en"
            }
