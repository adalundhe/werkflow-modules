from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetExportJobRequest(BaseModel):
    ApplicationId: StrictStr
    JobId: StrictStr
