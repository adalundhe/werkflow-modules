from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendTextSegment(BaseModel):
    Text: StrictStr
