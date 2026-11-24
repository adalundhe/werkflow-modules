from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LightsailUpdateLoadBalancerAttributeRequest(BaseModel):
    loadBalancerName: StrictStr
    attributeName: Literal['HealthCheckPath', 'SessionStickinessEnabled', 'SessionStickiness_LB_CookieDurationSeconds', 'HttpsRedirectionEnabled', 'TlsPolicyName']
    attributeValue: StrictStr
