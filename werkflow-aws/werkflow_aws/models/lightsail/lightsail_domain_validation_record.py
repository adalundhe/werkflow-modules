from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_dns_record_creation_state import LightsailDnsRecordCreationState
from .lightsail_resource_record import LightsailResourceRecord


class LightsailDomainValidationRecord(BaseModel):
    domainName: StrictStr | None = None
    resourceRecord: LightsailResourceRecord | None = None
    dnsRecordCreationState: LightsailDnsRecordCreationState | None = None
    validationStatus: StrictStr | None = None
