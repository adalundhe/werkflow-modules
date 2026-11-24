from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESMessageHeader(BaseModel):
    Name: StrictStr
    Value: StrictStr
