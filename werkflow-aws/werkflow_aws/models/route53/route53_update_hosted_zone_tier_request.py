from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class Route53UpdateHostedZoneTierRequest(BaseModel):
    HostedZoneId: StrictStr
    HostedZoneTier: Literal['STANDARD', 'ADVANCED']
    DryRun: StrictBool | None = None
