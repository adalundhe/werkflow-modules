from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .guard_duty_organization_statistics import GuardDutyOrganizationStatistics


class GuardDutyOrganizationDetails(BaseModel):
    UpdatedAt: datetime.datetime | StrictStr | None = None
    OrganizationStatistics: GuardDutyOrganizationStatistics | None = None
