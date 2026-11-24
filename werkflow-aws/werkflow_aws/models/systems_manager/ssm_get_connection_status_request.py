from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMGetConnectionStatusRequest(BaseModel):
    Target: StrictStr
