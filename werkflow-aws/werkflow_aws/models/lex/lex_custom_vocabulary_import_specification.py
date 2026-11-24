from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexCustomVocabularyImportSpecification(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
