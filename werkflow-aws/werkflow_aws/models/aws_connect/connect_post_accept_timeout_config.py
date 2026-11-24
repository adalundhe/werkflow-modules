from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ConnectPostAcceptTimeoutConfig(BaseModel):
    DurationInSeconds: StrictInt | None = None
