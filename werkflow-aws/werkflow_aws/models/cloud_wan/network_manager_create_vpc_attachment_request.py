from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .network_manager_nat_rule_request import NetworkManagerNatRuleRequest
from .network_manager_tag import NetworkManagerTag
from .network_manager_vpc_options import NetworkManagerVpcOptions


class NetworkManagerCreateVpcAttachmentRequest(BaseModel):
    CoreNetworkId: StrictStr
    VpcArn: StrictStr
    SubnetArns: list[StrictStr]
    Options: NetworkManagerVpcOptions | None = None
    RoutingPolicyLabel: StrictStr | None = None
    NatGatewaySupport: Literal['ENABLE', 'DISABLE'] | None = None
    NatGatewayRules: list[NetworkManagerNatRuleRequest] | None = None
    Tags: list[NetworkManagerTag] | None = None
    ClientToken: StrictStr | None = None
