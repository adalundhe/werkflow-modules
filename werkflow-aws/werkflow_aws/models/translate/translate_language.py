from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranslateLanguage(BaseModel):
    LanguageName: StrictStr | None = None
    LanguageCode: StrictStr | None = None
