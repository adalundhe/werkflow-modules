from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayUnprocessedTraceSegment(BaseModel):
    Id: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    Message: StrictStr | None = None
