from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubAwsEc2LaunchTemplateDataCpuOptionsDetails(BaseModel):
    CoreCount: StrictInt | None = None
    ThreadsPerCore: StrictInt | None = None
