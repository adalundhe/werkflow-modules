from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetImportJobRequest(BaseModel):
    ApplicationId: StrictStr
    JobId: StrictStr
