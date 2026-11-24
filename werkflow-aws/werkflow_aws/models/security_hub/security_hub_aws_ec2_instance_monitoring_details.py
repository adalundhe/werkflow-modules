from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2InstanceMonitoringDetails(BaseModel):
    State: StrictStr | None = None
