import pandas as pd
import os
from datetime import datetime


class AuditLogger:
    def __init__(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))

        log_dir = os.path.join(base_dir, "logs")
        os.makedirs(log_dir, exist_ok=True)

        self.log_path = os.path.join(log_dir, "audit_logs.csv")

        if not os.path.exists(self.log_path):
            pd.DataFrame(
                columns=[
                    "timestamp",
                    "status",
                    "decision"
                ]
            ).to_csv(self.log_path, index=False)

    def log(self, status, decision):

        new_log = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": status,
            "decision": decision
        }

        df = pd.read_csv(self.log_path)

        df = pd.concat(
            [df, pd.DataFrame([new_log])],
            ignore_index=True
        )

        df.to_csv(self.log_path, index=False)