from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ConnectAfterContactWorkConfig(BaseModel):
    AfterContactWorkTimeLimit: StrictInt | None = None
