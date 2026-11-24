from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubServiceNowProviderConfiguration(BaseModel):
    InstanceName: StrictStr
    SecretArn: StrictStr
