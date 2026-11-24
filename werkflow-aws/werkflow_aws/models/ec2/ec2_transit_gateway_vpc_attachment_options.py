from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayVpcAttachmentOptions(BaseModel):
    DnsSupport: StrictStr | None = None
    SecurityGroupReferencingSupport: StrictStr | None = None
    Ipv6Support: StrictStr | None = None
    ApplianceModeSupport: StrictStr | None = None
