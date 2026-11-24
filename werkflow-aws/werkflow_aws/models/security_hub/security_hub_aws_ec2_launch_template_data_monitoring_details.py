from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubAwsEc2LaunchTemplateDataMonitoringDetails(BaseModel):
    Enabled: StrictBool | None = None
