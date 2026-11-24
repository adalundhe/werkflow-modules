from __future__ import annotations
from pydantic import BaseModel
from .step_functions_cloud_watch_logs_log_group import StepFunctionsCloudWatchLogsLogGroup


class StepFunctionsLogDestination(BaseModel):
    cloudWatchLogsLogGroup: StepFunctionsCloudWatchLogsLogGroup | None = None
