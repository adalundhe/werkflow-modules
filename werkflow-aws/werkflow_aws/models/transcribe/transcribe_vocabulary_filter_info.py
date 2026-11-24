from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class TranscribeVocabularyFilterInfo(BaseModel):
    VocabularyFilterName: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
