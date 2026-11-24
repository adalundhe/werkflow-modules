from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class TranscribeListLanguageModelsRequest(BaseModel):
    StatusEquals: Literal['IN_PROGRESS', 'FAILED', 'COMPLETED'] | None = None
    NameContains: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
