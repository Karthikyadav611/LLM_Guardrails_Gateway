import json
from input_guard import InputGuard
from pii_detector import PIIDetector
from data_access_guard import DataAccessGuard
from policy_engine import PolicyEngine
from llm_client import LLMClient
from audit_logger import AuditLogger

class GuardrailsGateway:
    def __init__(self, api_key):
        self.input_guard = InputGuard()
        self.pii_detector = PIIDetector()
        self.data_guard = DataAccessGuard()
        self.policy_engine = PolicyEngine()
        self.llm = LLMClient(api_key)
        self.logger = AuditLogger()
        self.config = self.policy_engine.config

    def process_request(self, user_prompt, use_json=False):
        # 1. Input Guard (STRICT ENFORCEMENT CHECK)
        is_safe, security_report = self.input_guard.check_security(user_prompt)

        # Stop execution immediately if any risk score is recorded
        if not is_safe or security_report['risk_score'] > 0:
            self.logger.log("Blocked", security_report['decision'])
            return self.config['fallbacks']['safety_message'], "Blocked", security_report

        # 2. PII Detection
        pii_found = self.pii_detector.detect(user_prompt)
        if pii_found:
            return self.config['fallbacks']['safety_message'], "Blocked", {"decision": "PII Detected", "risk_score": 5, "reason": str(pii_found)}

        # 3. Data Access Guard
        allowed, dec, reason = self.data_guard.check_access(user_prompt)
        if not allowed:
            return self.config['fallbacks']['safety_message'], "Blocked", {"decision": dec, "risk_score": 5, "reason": reason}

        # 4. LLM Call - Only reached if all guards pass
        response = self.llm.generate(user_prompt)

        return response, "Allowed", {"decision": "Success", "risk_score": 0}
