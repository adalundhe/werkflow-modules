from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LambdaWaitSucceededDetails(BaseModel):
    Duration: StrictInt | None = None
