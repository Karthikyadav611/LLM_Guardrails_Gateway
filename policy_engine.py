import yaml
class PolicyEngine:
    def __init__(self, config_path="llm_guardrails_gateway/config/rules.yaml"):
        with open(config_path, 'r') as f: self.config = yaml.safe_load(f)
    def validate_content(self, text):
        for word in self.config['policy']['blocked_keywords']:
            if word in text.lower(): return False, f"Policy violation: {word}"
        return True, "Compliant"
