from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class SecurityHubUpdateSecurityHubConfigurationRequest(BaseModel):
    AutoEnableControls: StrictBool | None = None
    ControlFindingGenerator: Literal['STANDARD_CONTROL', 'SECURITY_CONTROL'] | None = None
