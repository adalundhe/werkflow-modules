from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_feature_detail import SecurityHubFeatureDetail


class SecurityHubDescribeSecurityHubV2Response(BaseModel):
    HubV2Arn: StrictStr | None = None
    SubscribedAt: StrictStr | None = None
    Features: dict[StrictStr, SecurityHubFeatureDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
