from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_front_response_headers_policy_remove_header import CloudFrontResponseHeadersPolicyRemoveHeader


class CloudFrontResponseHeadersPolicyRemoveHeadersConfig(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[CloudFrontResponseHeadersPolicyRemoveHeader] | None = None
