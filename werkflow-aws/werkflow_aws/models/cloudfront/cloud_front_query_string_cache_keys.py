from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFrontQueryStringCacheKeys(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[StrictStr] | None = None
