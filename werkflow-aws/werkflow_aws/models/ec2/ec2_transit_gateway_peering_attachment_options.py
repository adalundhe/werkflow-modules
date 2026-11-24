from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2TransitGatewayPeeringAttachmentOptions(BaseModel):
    DynamicRouting: StrictStr | None = None
    RequesterAllowMultipathResilience: StrictBool | None = None
    RequesterMultipathResilienceMode: StrictStr | None = None
    AccepterAllowMultipathResilience: StrictBool | None = None
    AccepterMultipathResilienceMode: StrictStr | None = None
    MultipathResilienceStatus: StrictStr | None = None
