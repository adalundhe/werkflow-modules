from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .lightsail_load_balancer_tls_certificate_domain_validation_record import LightsailLoadBalancerTlsCertificateDomainValidationRecord
from .lightsail_load_balancer_tls_certificate_renewal_summary import LightsailLoadBalancerTlsCertificateRenewalSummary
from .lightsail_resource_location import LightsailResourceLocation
from .lightsail_tag import LightsailTag


class LightsailLoadBalancerTlsCertificate(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    supportCode: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
    tags: list[LightsailTag] | None = None
    loadBalancerName: StrictStr | None = None
    isAttached: StrictBool | None = None
    status: StrictStr | None = None
    domainName: StrictStr | None = None
    domainValidationRecords: list[LightsailLoadBalancerTlsCertificateDomainValidationRecord] | None = None
    failureReason: StrictStr | None = None
    issuedAt: datetime.datetime | StrictStr | None = None
    issuer: StrictStr | None = None
    keyAlgorithm: StrictStr | None = None
    notAfter: datetime.datetime | StrictStr | None = None
    notBefore: datetime.datetime | StrictStr | None = None
    renewalSummary: LightsailLoadBalancerTlsCertificateRenewalSummary | None = None
    revocationReason: StrictStr | None = None
    revokedAt: datetime.datetime | StrictStr | None = None
    serial: StrictStr | None = None
    signatureAlgorithm: StrictStr | None = None
    subject: StrictStr | None = None
    subjectAlternativeNames: list[StrictStr] | None = None
