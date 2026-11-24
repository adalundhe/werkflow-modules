from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionGetLabelDetectionRequestMetadata(BaseModel):
    SortBy: StrictStr | None = None
    AggregateBy: StrictStr | None = None
