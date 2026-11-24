from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FirehoseDirectPutSourceDescription(BaseModel):
    ThroughputHintInMBs: StrictInt | None = None
