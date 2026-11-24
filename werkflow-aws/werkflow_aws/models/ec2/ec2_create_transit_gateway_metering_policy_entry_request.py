from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2CreateTransitGatewayMeteringPolicyEntryRequest(BaseModel):
    TransitGatewayMeteringPolicyId: StrictStr
    PolicyRuleNumber: StrictInt
    MeteredAccount: Literal['source-attachment-owner', 'destination-attachment-owner', 'transit-gateway-owner']
    SourceTransitGatewayAttachmentId: StrictStr | None = None
    SourceTransitGatewayAttachmentType: Literal['vpc', 'vpn', 'vpn-concentrator', 'direct-connect-gateway', 'connect', 'peering', 'tgw-peering', 'network-function', 'client-vpn'] | None = None
    SourceCidrBlock: StrictStr | None = None
    SourcePortRange: StrictStr | None = None
    DestinationTransitGatewayAttachmentId: StrictStr | None = None
    DestinationTransitGatewayAttachmentType: Literal['vpc', 'vpn', 'vpn-concentrator', 'direct-connect-gateway', 'connect', 'peering', 'tgw-peering', 'network-function', 'client-vpn'] | None = None
    DestinationCidrBlock: StrictStr | None = None
    DestinationPortRange: StrictStr | None = None
    Protocol: StrictStr | None = None
    DryRun: StrictBool | None = None
