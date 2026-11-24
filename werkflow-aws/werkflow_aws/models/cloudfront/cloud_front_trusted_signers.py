from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CloudFrontTrustedSigners(BaseModel):
    Enabled: StrictBool | None = None
    Quantity: StrictInt | None = None
    Items: list[StrictStr] | None = None
