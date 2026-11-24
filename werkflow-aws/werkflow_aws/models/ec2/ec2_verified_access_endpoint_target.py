from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2VerifiedAccessEndpointTarget(BaseModel):
    VerifiedAccessEndpointId: StrictStr | None = None
    VerifiedAccessEndpointTargetIpAddress: StrictStr | None = None
    VerifiedAccessEndpointTargetDns: StrictStr | None = None
