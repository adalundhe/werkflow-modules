from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SageMakerRemoteDebugConfig(BaseModel):
    EnableRemoteDebug: StrictBool | None = None
