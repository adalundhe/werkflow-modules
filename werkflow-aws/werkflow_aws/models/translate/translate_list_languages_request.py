from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class TranslateListLanguagesRequest(BaseModel):
    DisplayLanguageCode: Literal['de', 'en', 'es', 'fr', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
