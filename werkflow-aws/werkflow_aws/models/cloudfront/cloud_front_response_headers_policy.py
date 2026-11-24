from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_front_response_headers_policy_config import CloudFrontResponseHeadersPolicyConfig


class CloudFrontResponseHeadersPolicy(BaseModel):
    Id: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ResponseHeadersPolicyConfig: CloudFrontResponseHeadersPolicyConfig | None = None
