from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetails(BaseModel):
    LogGroupArn: StrictStr | None = None
