import json
from pydantic import ValidationError
from pii_detector import PIIDetector
class OutputGuard:
    def __init__(self): self.pii_detector = PIIDetector()
    def validate_json(self, content, schema_class):
        try:
            data = json.loads(content)
            schema_class(**data)
            return True, data
        except (json.JSONDecodeError, ValidationError) as e: return False, str(e)
    def check_leaks(self, text):
        leaks = self.pii_detector.detect(text)
        if leaks: return False, "PII Leakage detected"
        return True, "Safe"
