from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranslateGetParallelDataRequest(BaseModel):
    Name: StrictStr
