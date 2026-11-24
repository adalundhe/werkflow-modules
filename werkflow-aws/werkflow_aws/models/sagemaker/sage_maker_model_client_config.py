from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerModelClientConfig(BaseModel):
    InvocationsTimeoutInSeconds: StrictInt | None = None
    InvocationsMaxRetries: StrictInt | None = None
