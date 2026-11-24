from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .network_manager_nat_rule_request import NetworkManagerNatRuleRequest


class NetworkManagerUpdateAttachmentNatConfigurationRequest(BaseModel):
    AttachmentId: StrictStr
    NatGatewaySupport: Literal['ENABLE', 'DISABLE'] | None = None
    NatSystemRouteSupport: StrictBool | None = None
    NatGatewayRules: list[NetworkManagerNatRuleRequest] | None = None
    ClientToken: StrictStr | None = None
