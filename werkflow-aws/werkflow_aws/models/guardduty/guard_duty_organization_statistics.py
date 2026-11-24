from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .guard_duty_organization_feature_statistics import GuardDutyOrganizationFeatureStatistics


class GuardDutyOrganizationStatistics(BaseModel):
    TotalAccountsCount: StrictInt | None = None
    MemberAccountsCount: StrictInt | None = None
    ActiveAccountsCount: StrictInt | None = None
    EnabledAccountsCount: StrictInt | None = None
    CountByFeature: list[GuardDutyOrganizationFeatureStatistics] | None = None
