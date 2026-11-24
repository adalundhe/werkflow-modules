from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .translate_applied_terminology import TranslateAppliedTerminology
from .translate_translation_settings import TranslateTranslationSettings
from .translated_document import TranslatedDocument as _TranslatedDocumentType


class TranslateTranslateDocumentResponse(BaseModel):
    TranslatedDocument: _TranslatedDocumentType | None = None
    SourceLanguageCode: StrictStr | None = None
    TargetLanguageCode: StrictStr | None = None
    AppliedTerminologies: list[TranslateAppliedTerminology] | None = None
    AppliedSettings: TranslateTranslationSettings | None = None
    ResponseMetadata: dict[str, Any] | None = None
