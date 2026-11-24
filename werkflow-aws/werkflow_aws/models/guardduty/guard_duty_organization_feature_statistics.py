from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_organization_feature_statistics_additional_configuration import GuardDutyOrganizationFeatureStatisticsAdditionalConfiguration


class GuardDutyOrganizationFeatureStatistics(BaseModel):
    Name: StrictStr | None = None
    EnabledAccountsCount: StrictInt | None = None
    AdditionalConfiguration: list[GuardDutyOrganizationFeatureStatisticsAdditionalConfiguration] | None = None
