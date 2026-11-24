from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_wafv2_custom_response_details import SecurityHubAwsWafv2CustomResponseDetails


class SecurityHubAwsWafv2ActionBlockDetails(BaseModel):
    CustomResponse: SecurityHubAwsWafv2CustomResponseDetails | None = None
