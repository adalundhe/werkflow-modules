from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class TranscribeVocabularyInfo(BaseModel):
    VocabularyName: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    VocabularyState: StrictStr | None = None
