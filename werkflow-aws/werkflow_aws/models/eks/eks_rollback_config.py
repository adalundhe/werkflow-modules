from __future__ import annotations
from pydantic import BaseModel, StrictInt


class EKSRollbackConfig(BaseModel):
    timeoutMinutes: StrictInt | None = None
