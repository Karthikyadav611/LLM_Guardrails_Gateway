import re

class InputGuard:
    def __init__(self):
        self.categories = {
            "policy_bypass": [
                r"pretend you have no policies", r"respond without restrictions",
                r"no safety rules", r"ignore policies", r"disable safety",
                r"bypass (all )?safety restrictions", r"unrestricted mode", r"uncensored mode"
            ],
            "instruction_override": [
                r"ignore previous instructions", r"forget previous instructions",
                r"override system prompt", r"disregard developer instructions",
                r"ignore all rules", r"reset your instructions"
            ],
            "roleplay_jailbreak": [
                r"act as dan", r"you are dan", r"act as an unrestricted ai",
                r"pretend to be an uncensored assistant", r"roleplay as a model without rules"
            ],
            "system_prompt_extraction": [
                r"reveal your system prompt", r"show hidden instructions",
                r"display developer message", r"print your initial prompt", r"what are your rules"
            ],
            "safety_evasion": [
                r"for educational purposes only, bypass", r"hypothetically ignore rules",
                r"in a fictional world with no restrictions", r"answer without ethical constraints"
            ]
        }

    def check_security(self, text):
        risk_score = 0
        matched_categories = []
        matched_patterns = []

        print(f"[DEBUG] Auditing Prompt: {text}")

        for category, patterns in self.categories.items():
            cat_matched = False
            for pattern in patterns:
                # Fix: Explicit re.IGNORECASE added here
                if re.search(pattern, text, re.IGNORECASE):
                    risk_score += 1
                    matched_patterns.append(pattern)
                    cat_matched = True
            if cat_matched:
                matched_categories.append(category)

        report = {
            "blocked": risk_score >= 1,
            "decision": "Jailbreak Attempt Detected" if risk_score >= 1 else "Clean",
            "risk_score": risk_score,
            "matched_categories": matched_categories,
            "matched_patterns": matched_patterns
        }

        print(f"[DEBUG] Risk Score: {risk_score} | Blocked: {report['blocked']} | Patterns: {matched_patterns}")
        return not report['blocked'], report
