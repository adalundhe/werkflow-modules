from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetSegmentImportJobsRequest(BaseModel):
    ApplicationId: StrictStr
    SegmentId: StrictStr
    PageSize: StrictStr | None = None
    Token: StrictStr | None = None
