from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_wafv2_action_allow_details import SecurityHubAwsWafv2ActionAllowDetails
from .security_hub_aws_wafv2_action_block_details import SecurityHubAwsWafv2ActionBlockDetails


class SecurityHubAwsWafv2WebAclActionDetails(BaseModel):
    Allow: SecurityHubAwsWafv2ActionAllowDetails | None = None
    Block: SecurityHubAwsWafv2ActionBlockDetails | None = None
