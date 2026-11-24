from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionGetFaceLivenessSessionResultsRequest(BaseModel):
    SessionId: StrictStr
