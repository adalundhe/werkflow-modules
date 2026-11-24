from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_encryption_support import EC2EncryptionSupport


class EC2TransitGatewayOptions(BaseModel):
    AmazonSideAsn: StrictInt | None = None
    TransitGatewayCidrBlocks: list[StrictStr] | None = None
    AutoAcceptSharedAttachments: StrictStr | None = None
    DefaultRouteTableAssociation: StrictStr | None = None
    AssociationDefaultRouteTableId: StrictStr | None = None
    DefaultRouteTablePropagation: StrictStr | None = None
    PropagationDefaultRouteTableId: StrictStr | None = None
    VpnEcmpSupport: StrictStr | None = None
    DnsSupport: StrictStr | None = None
    SecurityGroupReferencingSupport: StrictStr | None = None
    MulticastSupport: StrictStr | None = None
    EncryptionSupport: EC2EncryptionSupport | None = None
