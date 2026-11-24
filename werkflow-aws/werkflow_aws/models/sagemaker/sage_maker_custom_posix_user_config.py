from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerCustomPosixUserConfig(BaseModel):
    Uid: StrictInt | None = None
    Gid: StrictInt | None = None
