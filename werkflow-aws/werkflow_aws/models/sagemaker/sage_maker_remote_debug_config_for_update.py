from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SageMakerRemoteDebugConfigForUpdate(BaseModel):
    EnableRemoteDebug: StrictBool | None = None
