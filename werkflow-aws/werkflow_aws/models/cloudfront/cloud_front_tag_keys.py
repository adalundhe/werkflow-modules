from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontTagKeys(BaseModel):
    Items: list[StrictStr] | None = None
