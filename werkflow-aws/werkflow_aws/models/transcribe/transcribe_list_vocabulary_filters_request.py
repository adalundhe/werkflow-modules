from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TranscribeListVocabularyFiltersRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NameContains: StrictStr | None = None
