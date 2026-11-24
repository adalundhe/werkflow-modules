from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubAwsAutoScalingLaunchConfigurationInstanceMonitoringDetails(BaseModel):
    Enabled: StrictBool | None = None
