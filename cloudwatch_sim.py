import boto3
from datetime import datetime, timedelta

class CloudWatchClient:
    def __init__(self, log_group):
        self.client = boto3.client("logs")
        self.log_group = log_group

    def fetch_logs(self, limit=50):
        """
        Fetch latest logs from AWS CloudWatch Logs
        """

        end_time = int(datetime.utcnow().timestamp() * 1000)
        start_time = int((datetime.utcnow() - timedelta(hours=1)).timestamp() * 1000)

        response = self.client.filter_log_events(
            logGroupName=self.log_group,
            startTime=start_time,
            endTime=end_time,
            limit=limit
        )

        logs = []

        for event in response.get("events", []):
            logs.append({
                "timestamp": event["timestamp"],
                "message": event["message"]
            })

        return logs