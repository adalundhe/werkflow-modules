from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MWAADimension(BaseModel):
    Name: StrictStr
    Value: StrictStr
