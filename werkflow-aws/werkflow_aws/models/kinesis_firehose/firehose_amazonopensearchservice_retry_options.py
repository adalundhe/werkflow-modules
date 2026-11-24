from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FirehoseAmazonopensearchserviceRetryOptions(BaseModel):
    DurationInSeconds: StrictInt | None = None
