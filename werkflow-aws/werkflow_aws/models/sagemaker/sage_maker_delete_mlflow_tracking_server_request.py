from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteMlflowTrackingServerRequest(BaseModel):
    TrackingServerName: StrictStr
