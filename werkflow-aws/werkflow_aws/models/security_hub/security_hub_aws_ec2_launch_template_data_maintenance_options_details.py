from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2LaunchTemplateDataMaintenanceOptionsDetails(BaseModel):
    AutoRecovery: StrictStr | None = None
