from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractGetAdapterRequest(BaseModel):
    AdapterId: StrictStr
