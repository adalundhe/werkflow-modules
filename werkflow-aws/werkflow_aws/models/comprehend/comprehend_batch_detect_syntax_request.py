from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComprehendBatchDetectSyntaxRequest(BaseModel):
    TextList: list[StrictStr]
    LanguageCode: Literal['en', 'es', 'fr', 'de', 'it', 'pt']
