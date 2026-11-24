from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EC2TransitGatewayRequestOptions(BaseModel):
    AmazonSideAsn: StrictInt | None = None
    AutoAcceptSharedAttachments: Literal['enable', 'disable'] | None = None
    DefaultRouteTableAssociation: Literal['enable', 'disable'] | None = None
    DefaultRouteTablePropagation: Literal['enable', 'disable'] | None = None
    VpnEcmpSupport: Literal['enable', 'disable'] | None = None
    DnsSupport: Literal['enable', 'disable'] | None = None
    SecurityGroupReferencingSupport: Literal['enable', 'disable'] | None = None
    MulticastSupport: Literal['enable', 'disable'] | None = None
    TransitGatewayCidrBlocks: list[StrictStr] | None = None
