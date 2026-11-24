from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EC2ModifyTransitGatewayOptions(BaseModel):
    AddTransitGatewayCidrBlocks: list[StrictStr] | None = None
    RemoveTransitGatewayCidrBlocks: list[StrictStr] | None = None
    VpnEcmpSupport: Literal['enable', 'disable'] | None = None
    DnsSupport: Literal['enable', 'disable'] | None = None
    SecurityGroupReferencingSupport: Literal['enable', 'disable'] | None = None
    AutoAcceptSharedAttachments: Literal['enable', 'disable'] | None = None
    DefaultRouteTableAssociation: Literal['enable', 'disable'] | None = None
    AssociationDefaultRouteTableId: StrictStr | None = None
    DefaultRouteTablePropagation: Literal['enable', 'disable'] | None = None
    PropagationDefaultRouteTableId: StrictStr | None = None
    AmazonSideAsn: StrictInt | None = None
    EncryptionSupport: Literal['enable', 'disable'] | None = None
