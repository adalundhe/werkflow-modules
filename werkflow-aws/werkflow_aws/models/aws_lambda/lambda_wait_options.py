from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LambdaWaitOptions(BaseModel):
    WaitSeconds: StrictInt | None = None
