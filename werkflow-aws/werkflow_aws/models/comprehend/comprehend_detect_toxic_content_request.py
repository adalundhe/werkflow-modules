from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .comprehend_text_segment import ComprehendTextSegment


class ComprehendDetectToxicContentRequest(BaseModel):
    TextSegments: list[ComprehendTextSegment]
    LanguageCode: Literal['en', 'es', 'fr', 'de', 'it', 'pt', 'ar', 'hi', 'ja', 'ko', 'zh', 'zh-TW']
