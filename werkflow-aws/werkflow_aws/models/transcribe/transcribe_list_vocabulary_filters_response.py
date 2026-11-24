from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transcribe_vocabulary_filter_info import TranscribeVocabularyFilterInfo


class TranscribeListVocabularyFiltersResponse(BaseModel):
    NextToken: StrictStr | None = None
    VocabularyFilters: list[TranscribeVocabularyFilterInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
