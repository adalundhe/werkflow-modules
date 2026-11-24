from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SupportUploadRange(BaseModel):
    startIndex: StrictInt
    endIndex: StrictInt | None = None
