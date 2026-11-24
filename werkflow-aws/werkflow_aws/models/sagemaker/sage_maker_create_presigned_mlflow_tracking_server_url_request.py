from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerCreatePresignedMlflowTrackingServerUrlRequest(BaseModel):
    TrackingServerName: StrictStr
    ExpiresInSeconds: StrictInt | None = None
    SessionExpirationDurationInSeconds: StrictInt | None = None
