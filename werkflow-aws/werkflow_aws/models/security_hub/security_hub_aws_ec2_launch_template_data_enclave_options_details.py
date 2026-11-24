from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubAwsEc2LaunchTemplateDataEnclaveOptionsDetails(BaseModel):
    Enabled: StrictBool | None = None
