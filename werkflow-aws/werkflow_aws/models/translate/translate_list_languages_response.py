from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .translate_language import TranslateLanguage


class TranslateListLanguagesResponse(BaseModel):
    Languages: list[TranslateLanguage] | None = None
    DisplayLanguageCode: StrictStr | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
