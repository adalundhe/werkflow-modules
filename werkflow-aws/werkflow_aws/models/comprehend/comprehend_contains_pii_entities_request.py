from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComprehendContainsPiiEntitiesRequest(BaseModel):
    Text: StrictStr
    LanguageCode: Literal['en', 'es', 'fr', 'de', 'it', 'pt', 'ar', 'hi', 'ja', 'ko', 'zh', 'zh-TW']
