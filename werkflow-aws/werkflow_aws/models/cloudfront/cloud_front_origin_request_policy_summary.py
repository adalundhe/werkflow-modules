from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_origin_request_policy import CloudFrontOriginRequestPolicy


class CloudFrontOriginRequestPolicySummary(BaseModel):
    Type: StrictStr | None = None
    OriginRequestPolicy: CloudFrontOriginRequestPolicy | None = None
