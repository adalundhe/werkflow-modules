from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailLoadBalancerTlsCertificateDomainValidationOption(BaseModel):
    domainName: StrictStr | None = None
    validationStatus: StrictStr | None = None
