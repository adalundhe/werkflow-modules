from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CloudFrontTrustedKeyGroups(BaseModel):
    Enabled: StrictBool | None = None
    Quantity: StrictInt | None = None
    Items: list[StrictStr] | None = None
