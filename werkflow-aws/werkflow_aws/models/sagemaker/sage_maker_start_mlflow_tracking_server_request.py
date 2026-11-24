from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStartMlflowTrackingServerRequest(BaseModel):
    TrackingServerName: StrictStr
