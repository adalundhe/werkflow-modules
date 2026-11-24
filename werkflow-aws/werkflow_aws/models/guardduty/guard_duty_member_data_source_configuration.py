from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_data_source_configurations_result import GuardDutyDataSourceConfigurationsResult
from .guard_duty_member_features_configuration_result import GuardDutyMemberFeaturesConfigurationResult


class GuardDutyMemberDataSourceConfiguration(BaseModel):
    AccountId: StrictStr | None = None
    DataSources: GuardDutyDataSourceConfigurationsResult | None = None
    Features: list[GuardDutyMemberFeaturesConfigurationResult] | None = None
