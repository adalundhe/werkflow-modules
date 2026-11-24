from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class TranscribeVocabularyFilterEntry(BaseModel):
    Language: Literal['en', 'es', 'fr', 'it', 'de', 'ja', 'pt', 'ko', 'zh-CN', 'zh-TW', 'zh-HK']
    VocabularyFilterName: StrictStr | None = None
    Words: list[StrictStr] | None = None
