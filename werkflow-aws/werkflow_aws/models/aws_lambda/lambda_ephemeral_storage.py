from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LambdaEphemeralStorage(BaseModel):
    Size: StrictInt
