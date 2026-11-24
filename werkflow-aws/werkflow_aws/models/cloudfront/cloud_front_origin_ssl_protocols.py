from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFrontOriginSslProtocols(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[StrictStr] | None = None
