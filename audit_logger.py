import pandas as pd
import os
from datetime import datetime
class AuditLogger:
    def __init__(self, log_path="llm_guardrails_gateway/logs/audit_logs.csv"):
        self.log_path = log_path
        if not os.path.exists(log_path):
            pd.DataFrame(columns=["timestamp", "status", "decision"]).to_csv(log_path, index=False)
    def log(self, status, decision):
        new_log = {"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "status": status, "decision": decision}
        df = pd.read_csv(self.log_path)
        df = pd.concat([df, pd.DataFrame([new_log])], ignore_index=True)
        df.to_csv(self.log_path, index=False)
