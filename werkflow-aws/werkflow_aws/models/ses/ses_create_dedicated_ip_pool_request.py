from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ses_tag import SESTag


class SESCreateDedicatedIpPoolRequest(BaseModel):
    PoolName: StrictStr
    Tags: list[SESTag] | None = None
    ScalingMode: Literal['STANDARD', 'MANAGED'] | None = None
