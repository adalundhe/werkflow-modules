from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_client_vpn_authorization_rule_status import EC2ClientVpnAuthorizationRuleStatus


class EC2RevokeClientVpnIngressResponse(BaseModel):
    Status: EC2ClientVpnAuthorizationRuleStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
