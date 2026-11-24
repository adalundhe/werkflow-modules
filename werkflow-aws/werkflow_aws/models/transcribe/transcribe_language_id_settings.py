from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeLanguageIdSettings(BaseModel):
    VocabularyName: StrictStr | None = None
    VocabularyFilterName: StrictStr | None = None
    LanguageModelName: StrictStr | None = None
