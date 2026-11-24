from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendBatchDetectDominantLanguageRequest(BaseModel):
    TextList: list[StrictStr]
