from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeDeleteCallAnalyticsCategoryRequest(BaseModel):
    CategoryName: StrictStr
