from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MediaStoreCorsRule(BaseModel):
    AllowedOrigins: list[StrictStr] | None = None
    AllowedMethods: list[StrictStr] | None = None
    AllowedHeaders: list[StrictStr] | None = None
    MaxAgeSeconds: StrictInt | None = None
    ExposeHeaders: list[StrictStr] | None = None
