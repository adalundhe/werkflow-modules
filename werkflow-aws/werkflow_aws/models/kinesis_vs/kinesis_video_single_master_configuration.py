from __future__ import annotations
from pydantic import BaseModel, StrictInt


class KinesisVideoSingleMasterConfiguration(BaseModel):
    MessageTtlSeconds: StrictInt | None = None
