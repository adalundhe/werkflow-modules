from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class RekognitionGetCelebrityRecognitionRequest(BaseModel):
    JobId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    SortBy: Literal['ID', 'TIMESTAMP'] | None = None
