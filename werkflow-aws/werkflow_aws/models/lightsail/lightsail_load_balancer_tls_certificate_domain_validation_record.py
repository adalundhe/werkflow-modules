from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_load_balancer_tls_certificate_dns_record_creation_state import LightsailLoadBalancerTlsCertificateDnsRecordCreationState


class LightsailLoadBalancerTlsCertificateDomainValidationRecord(BaseModel):
    name: StrictStr | None = None
    type: StrictStr | None = None
    value: StrictStr | None = None
    validationStatus: StrictStr | None = None
    domainName: StrictStr | None = None
    dnsRecordCreationState: LightsailLoadBalancerTlsCertificateDnsRecordCreationState | None = None
