from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lightsail_domain_validation_record import LightsailDomainValidationRecord


class LightsailRenewalSummary(BaseModel):
    domainValidationRecords: list[LightsailDomainValidationRecord] | None = None
    renewalStatus: StrictStr | None = None
    renewalStatusReason: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
