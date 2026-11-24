from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMTag(BaseModel):
    Key: StrictStr
    Value: StrictStr
