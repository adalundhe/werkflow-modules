from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RekognitionGetSegmentDetectionRequest(BaseModel):
    JobId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
