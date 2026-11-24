from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayMeteringPolicyRule(BaseModel):
    SourceTransitGatewayAttachmentId: StrictStr | None = None
    SourceTransitGatewayAttachmentType: StrictStr | None = None
    SourceCidrBlock: StrictStr | None = None
    SourcePortRange: StrictStr | None = None
    DestinationTransitGatewayAttachmentId: StrictStr | None = None
    DestinationTransitGatewayAttachmentType: StrictStr | None = None
    DestinationCidrBlock: StrictStr | None = None
    DestinationPortRange: StrictStr | None = None
    Protocol: StrictStr | None = None
