from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetExportJobsRequest(BaseModel):
    ApplicationId: StrictStr
    PageSize: StrictStr | None = None
    Token: StrictStr | None = None
