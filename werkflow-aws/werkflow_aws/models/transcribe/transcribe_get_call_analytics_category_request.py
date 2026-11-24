from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeGetCallAnalyticsCategoryRequest(BaseModel):
    CategoryName: StrictStr
