from __future__ import annotations
from pydantic import BaseModel, StrictStr


class STSTag(BaseModel):
    Key: StrictStr
    Value: StrictStr
