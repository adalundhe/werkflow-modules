from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_origin_request_policy_list import CloudFrontOriginRequestPolicyList


class CloudFrontListOriginRequestPoliciesResponse(BaseModel):
    OriginRequestPolicyList: CloudFrontOriginRequestPolicyList | None = None
    ResponseMetadata: dict[str, Any] | None = None
