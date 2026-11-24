from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class RekognitionGetFaceSearchRequest(BaseModel):
    JobId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    SortBy: Literal['INDEX', 'TIMESTAMP'] | None = None
