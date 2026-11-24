from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontCacheTagConfig(BaseModel):
    HeaderName: StrictStr | None = None
