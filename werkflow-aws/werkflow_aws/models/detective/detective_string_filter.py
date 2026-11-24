from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveStringFilter(BaseModel):
    Value: StrictStr
