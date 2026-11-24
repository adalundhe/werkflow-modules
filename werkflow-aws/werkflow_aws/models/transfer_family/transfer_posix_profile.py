from __future__ import annotations
from pydantic import BaseModel, StrictInt


class TransferPosixProfile(BaseModel):
    Uid: StrictInt | None = None
    Gid: StrictInt | None = None
    SecondaryGids: list[StrictInt] | None = None
