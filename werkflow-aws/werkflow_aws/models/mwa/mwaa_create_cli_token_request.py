from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MWAACreateCliTokenRequest(BaseModel):
    Name: StrictStr
