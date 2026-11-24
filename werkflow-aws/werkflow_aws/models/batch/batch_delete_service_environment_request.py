from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchDeleteServiceEnvironmentRequest(BaseModel):
    serviceEnvironment: StrictStr
