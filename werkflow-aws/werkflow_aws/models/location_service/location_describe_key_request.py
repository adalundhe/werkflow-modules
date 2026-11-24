from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationDescribeKeyRequest(BaseModel):
    KeyName: StrictStr
