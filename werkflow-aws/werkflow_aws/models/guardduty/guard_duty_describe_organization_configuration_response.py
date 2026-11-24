from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .guard_duty_organization_data_source_configurations_result import GuardDutyOrganizationDataSourceConfigurationsResult
from .guard_duty_organization_feature_configuration_result import GuardDutyOrganizationFeatureConfigurationResult


class GuardDutyDescribeOrganizationConfigurationResponse(BaseModel):
    AutoEnable: StrictBool | None = None
    MemberAccountLimitReached: StrictBool | None = None
    DataSources: GuardDutyOrganizationDataSourceConfigurationsResult | None = None
    Features: list[GuardDutyOrganizationFeatureConfigurationResult] | None = None
    NextToken: StrictStr | None = None
    AutoEnableOrganizationMembers: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
