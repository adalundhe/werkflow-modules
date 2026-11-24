from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WAFv2GetEventRequest(BaseModel):
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    EventId: StrictStr
    WebAclArn: StrictStr
