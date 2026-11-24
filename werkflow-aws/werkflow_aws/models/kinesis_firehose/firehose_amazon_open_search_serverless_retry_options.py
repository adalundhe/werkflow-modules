from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FirehoseAmazonOpenSearchServerlessRetryOptions(BaseModel):
    DurationInSeconds: StrictInt | None = None
