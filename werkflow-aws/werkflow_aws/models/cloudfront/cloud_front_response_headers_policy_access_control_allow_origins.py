from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFrontResponseHeadersPolicyAccessControlAllowOrigins(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[StrictStr] | None = None
