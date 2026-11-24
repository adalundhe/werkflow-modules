from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_load_balancer_tls_certificate_domain_validation_option import LightsailLoadBalancerTlsCertificateDomainValidationOption


class LightsailLoadBalancerTlsCertificateRenewalSummary(BaseModel):
    renewalStatus: StrictStr | None = None
    domainValidationOptions: list[LightsailLoadBalancerTlsCertificateDomainValidationOption] | None = None
