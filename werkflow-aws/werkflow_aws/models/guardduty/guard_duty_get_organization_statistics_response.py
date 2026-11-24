from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .guard_duty_organization_details import GuardDutyOrganizationDetails


class GuardDutyGetOrganizationStatisticsResponse(BaseModel):
    OrganizationDetails: GuardDutyOrganizationDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
