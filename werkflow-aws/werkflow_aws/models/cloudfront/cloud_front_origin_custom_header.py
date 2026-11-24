from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontOriginCustomHeader(BaseModel):
    HeaderName: StrictStr | None = None
    HeaderValue: StrictStr | None = None
