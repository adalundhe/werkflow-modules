from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFrontFieldPatterns(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[StrictStr] | None = None
