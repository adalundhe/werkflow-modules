from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSessionTag(BaseModel):
    Key: StrictStr
    Value: StrictStr
