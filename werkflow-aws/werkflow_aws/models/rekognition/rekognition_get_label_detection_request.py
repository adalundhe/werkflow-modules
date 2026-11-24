from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class RekognitionGetLabelDetectionRequest(BaseModel):
    JobId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    SortBy: Literal['NAME', 'TIMESTAMP'] | None = None
    AggregateBy: Literal['TIMESTAMPS', 'SEGMENTS'] | None = None
