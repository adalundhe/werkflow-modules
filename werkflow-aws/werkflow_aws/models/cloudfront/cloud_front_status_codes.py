from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CloudFrontStatusCodes(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[StrictInt] | None = None
