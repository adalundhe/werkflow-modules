from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityLakeDataLakeLifecycleExpiration(BaseModel):
    days: StrictInt | None = None
