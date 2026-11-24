from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayMulticastDomainOptions(BaseModel):
    Igmpv2Support: StrictStr | None = None
    StaticSourcesSupport: StrictStr | None = None
    AutoAcceptSharedAssociations: StrictStr | None = None
