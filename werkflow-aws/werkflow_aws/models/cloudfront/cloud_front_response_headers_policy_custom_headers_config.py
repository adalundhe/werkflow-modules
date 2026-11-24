from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_front_response_headers_policy_custom_header import CloudFrontResponseHeadersPolicyCustomHeader


class CloudFrontResponseHeadersPolicyCustomHeadersConfig(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[CloudFrontResponseHeadersPolicyCustomHeader] | None = None
