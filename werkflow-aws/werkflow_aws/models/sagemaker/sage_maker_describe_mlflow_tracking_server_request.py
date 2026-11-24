from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeMlflowTrackingServerRequest(BaseModel):
    TrackingServerName: StrictStr
