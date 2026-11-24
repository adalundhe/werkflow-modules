from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetails(BaseModel):
    Max: StrictInt | None = None
    Min: StrictInt | None = None
