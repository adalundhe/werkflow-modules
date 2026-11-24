from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_front_origin_request_policy_config import CloudFrontOriginRequestPolicyConfig


class CloudFrontOriginRequestPolicy(BaseModel):
    Id: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    OriginRequestPolicyConfig: CloudFrontOriginRequestPolicyConfig | None = None
