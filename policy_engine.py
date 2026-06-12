import os
import yaml


class PolicyEngine:
    def __init__(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))

        config_path = os.path.join(
            base_dir,
            "config",
            "rules.yaml"
        )

        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

    def validate_content(self, text):

        text = text.lower()

        for word in self.config["policy"]["blocked_keywords"]:
            if word.lower() in text:
                return False, f"Policy violation: {word}"

        return True, "Compliant"