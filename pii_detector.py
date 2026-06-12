import re
class PIIDetector:
    def __init__(self):
        self.patterns = {
            "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            "phone": r"\b\d{10}\b",
            "aadhaar": r"\b\d{4}\s?\d{4}\s?\d{4}\b",
            "pan": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"
        }
    def detect(self, text):
        found = []
        for pii_type, pattern in self.patterns.items():
            if re.search(pattern, text):
                found.append(pii_type.capitalize())
        return found
    def mask(self, text):
        for pii_type, pattern in self.patterns.items():
            text = re.sub(pattern, "[MASKED]", text)
        return text
