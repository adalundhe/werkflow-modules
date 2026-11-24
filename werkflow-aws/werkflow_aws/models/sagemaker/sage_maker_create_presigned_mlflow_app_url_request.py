from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerCreatePresignedMlflowAppUrlRequest(BaseModel):
    Arn: StrictStr
    ExpiresInSeconds: StrictInt | None = None
    SessionExpirationDurationInSeconds: StrictInt | None = None
