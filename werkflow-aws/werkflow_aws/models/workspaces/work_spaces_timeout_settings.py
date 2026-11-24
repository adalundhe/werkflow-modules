from __future__ import annotations
from pydantic import BaseModel, StrictInt


class WorkSpacesTimeoutSettings(BaseModel):
    DisconnectTimeoutInSeconds: StrictInt | None = None
    IdleDisconnectTimeoutInSeconds: StrictInt | None = None
    MaxUserDurationInSeconds: StrictInt | None = None
