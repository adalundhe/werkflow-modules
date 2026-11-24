from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsEc2TransitGatewayDetails(BaseModel):
    Id: StrictStr | None = None
    Description: StrictStr | None = None
    DefaultRouteTablePropagation: StrictStr | None = None
    AutoAcceptSharedAttachments: StrictStr | None = None
    DefaultRouteTableAssociation: StrictStr | None = None
    TransitGatewayCidrBlocks: list[StrictStr] | None = None
    AssociationDefaultRouteTableId: StrictStr | None = None
    PropagationDefaultRouteTableId: StrictStr | None = None
    VpnEcmpSupport: StrictStr | None = None
    DnsSupport: StrictStr | None = None
    MulticastSupport: StrictStr | None = None
    AmazonSideAsn: StrictInt | None = None
