from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_headers import CloudFrontHeaders


class CloudFrontCachePolicyHeadersConfig(BaseModel):
    HeaderBehavior: StrictStr | None = None
    Headers: CloudFrontHeaders | None = None
