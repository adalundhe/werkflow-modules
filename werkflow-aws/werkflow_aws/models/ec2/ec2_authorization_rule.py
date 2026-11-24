from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_client_vpn_authorization_rule_status import EC2ClientVpnAuthorizationRuleStatus


class EC2AuthorizationRule(BaseModel):
    ClientVpnEndpointId: StrictStr | None = None
    Description: StrictStr | None = None
    GroupId: StrictStr | None = None
    AccessAll: StrictBool | None = None
    DestinationCidr: StrictStr | None = None
    Status: EC2ClientVpnAuthorizationRuleStatus | None = None
