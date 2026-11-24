from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FirehoseElasticsearchBufferingHints(BaseModel):
    IntervalInSeconds: StrictInt | None = None
    SizeInMBs: StrictInt | None = None
