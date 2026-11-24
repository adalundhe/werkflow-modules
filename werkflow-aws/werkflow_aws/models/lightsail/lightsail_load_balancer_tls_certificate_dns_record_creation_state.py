from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailLoadBalancerTlsCertificateDnsRecordCreationState(BaseModel):
    code: StrictStr | None = None
    message: StrictStr | None = None
