from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FirehoseElasticsearchRetryOptions(BaseModel):
    DurationInSeconds: StrictInt | None = None
