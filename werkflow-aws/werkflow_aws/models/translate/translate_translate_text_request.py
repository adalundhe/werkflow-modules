from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .translate_translation_settings import TranslateTranslationSettings


class TranslateTranslateTextRequest(BaseModel):
    Text: StrictStr
    SourceLanguageCode: StrictStr
    TargetLanguageCode: StrictStr
    TerminologyNames: list[StrictStr] | None = None
    Settings: TranslateTranslationSettings | None = None
