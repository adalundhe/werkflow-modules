from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .lightsail_domain_validation_record import LightsailDomainValidationRecord
from .lightsail_renewal_summary import LightsailRenewalSummary
from .lightsail_tag import LightsailTag


class LightsailCertificate(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    domainName: StrictStr | None = None
    status: StrictStr | None = None
    serialNumber: StrictStr | None = None
    subjectAlternativeNames: list[StrictStr] | None = None
    domainValidationRecords: list[LightsailDomainValidationRecord] | None = None
    requestFailureReason: StrictStr | None = None
    inUseResourceCount: StrictInt | None = None
    keyAlgorithm: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    issuedAt: datetime.datetime | StrictStr | None = None
    issuerCA: StrictStr | None = None
    notBefore: datetime.datetime | StrictStr | None = None
    notAfter: datetime.datetime | StrictStr | None = None
    eligibleToRenew: StrictStr | None = None
    renewalSummary: LightsailRenewalSummary | None = None
    revokedAt: datetime.datetime | StrictStr | None = None
    revocationReason: StrictStr | None = None
    tags: list[LightsailTag] | None = None
    supportCode: StrictStr | None = None
