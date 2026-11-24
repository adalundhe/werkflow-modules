from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ECSTimeoutConfiguration(BaseModel):
    idleTimeoutSeconds: StrictInt | None = None
    perRequestTimeoutSeconds: StrictInt | None = None
