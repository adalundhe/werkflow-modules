from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ConnectRoutingCriteriaInputStepExpiry(BaseModel):
    DurationInSeconds: StrictInt | None = None
