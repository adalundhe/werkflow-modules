from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .guard_duty_coverage_resource_details import GuardDutyCoverageResourceDetails


class GuardDutyCoverageResource(BaseModel):
    ResourceId: StrictStr | None = None
    DetectorId: StrictStr | None = None
    AccountId: StrictStr | None = None
    ResourceDetails: GuardDutyCoverageResourceDetails | None = None
    CoverageStatus: StrictStr | None = None
    Issue: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
