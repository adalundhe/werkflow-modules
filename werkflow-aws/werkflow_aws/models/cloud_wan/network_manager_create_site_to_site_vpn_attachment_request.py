from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .network_manager_nat_rule_request import NetworkManagerNatRuleRequest
from .network_manager_tag import NetworkManagerTag


class NetworkManagerCreateSiteToSiteVpnAttachmentRequest(BaseModel):
    CoreNetworkId: StrictStr
    VpnConnectionArn: StrictStr
    RoutingPolicyLabel: StrictStr | None = None
    NatGatewaySupport: Literal['ENABLE', 'DISABLE'] | None = None
    NatSystemRouteSupport: StrictBool | None = None
    NatGatewayRules: list[NetworkManagerNatRuleRequest] | None = None
    Tags: list[NetworkManagerTag] | None = None
    ClientToken: StrictStr | None = None
