from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class TranscribeListMedicalVocabulariesRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    StateEquals: Literal['PENDING', 'READY', 'FAILED'] | None = None
    NameContains: StrictStr | None = None
