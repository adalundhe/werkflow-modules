from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubEnableSecurityHubRequest(BaseModel):
    Tags: dict[StrictStr, StrictStr] | None = None
    EnableDefaultStandards: StrictBool | None = None
    ControlFindingGenerator: Literal['STANDARD_CONTROL', 'SECURITY_CONTROL'] | None = None
