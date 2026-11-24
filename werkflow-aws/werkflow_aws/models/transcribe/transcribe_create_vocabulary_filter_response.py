from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class TranscribeCreateVocabularyFilterResponse(BaseModel):
    VocabularyFilterName: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
