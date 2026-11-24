from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WAFv2GetEventActorRequest(BaseModel):
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    EventActorId: StrictStr
