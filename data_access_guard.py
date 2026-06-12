import re
import yaml
class DataAccessGuard:
    def __init__(self):
        self.sensitive_patterns = [
            r"customer (data|details|records|database)",
            r"employee (records|salaries|data)",
            r"internal data",
            r"confidential data",
            r"sensitive records"
        ]
    def check_access(self, text):
        for pattern in self.sensitive_patterns:
            if re.search(pattern, text.lower()):
                return False, "Sensitive Data Request", "Authorization Required: " + pattern
        return True, "Passed", ""
