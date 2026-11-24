from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class SecurityHubDisableSecurityHubFeatureV2Request(BaseModel):
    FeatureName: Literal['NETWORK_SCANNING']
