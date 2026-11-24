from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranslateTranslationSettings(BaseModel):
    Formality: StrictStr | None = None
    Profanity: StrictStr | None = None
    Brevity: StrictStr | None = None
