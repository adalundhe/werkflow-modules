from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .network_manager_connect_attachment_options import NetworkManagerConnectAttachmentOptions
from .network_manager_nat_rule_request import NetworkManagerNatRuleRequest
from .network_manager_tag import NetworkManagerTag


class NetworkManagerCreateConnectAttachmentRequest(BaseModel):
    CoreNetworkId: StrictStr
    EdgeLocation: StrictStr
    TransportAttachmentId: StrictStr
    Options: NetworkManagerConnectAttachmentOptions
    RoutingPolicyLabel: StrictStr | None = None
    NatGatewaySupport: Literal['ENABLE', 'DISABLE'] | None = None
    NatGatewayRules: list[NetworkManagerNatRuleRequest] | None = None
    Tags: list[NetworkManagerTag] | None = None
    ClientToken: StrictStr | None = None
