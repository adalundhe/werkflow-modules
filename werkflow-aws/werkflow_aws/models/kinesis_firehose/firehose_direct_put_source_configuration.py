from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FirehoseDirectPutSourceConfiguration(BaseModel):
    ThroughputHintInMBs: StrictInt
