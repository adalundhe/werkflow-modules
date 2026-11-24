from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class SecurityHubAwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails(BaseModel):
    Max: StrictFloat | StrictInt | None = None
    Min: StrictFloat | StrictInt | None = None
