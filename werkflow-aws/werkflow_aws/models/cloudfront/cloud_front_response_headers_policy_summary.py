from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_response_headers_policy import CloudFrontResponseHeadersPolicy


class CloudFrontResponseHeadersPolicySummary(BaseModel):
    Type: StrictStr | None = None
    ResponseHeadersPolicy: CloudFrontResponseHeadersPolicy | None = None
