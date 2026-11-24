from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MWAAGetEnvironmentRequest(BaseModel):
    Name: StrictStr
