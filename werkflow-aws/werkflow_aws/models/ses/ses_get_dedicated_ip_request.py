from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetDedicatedIpRequest(BaseModel):
    Ip: StrictStr
