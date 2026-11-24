from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_data_sources_free_trial import GuardDutyDataSourcesFreeTrial
from .guard_duty_free_trial_feature_configuration_result import GuardDutyFreeTrialFeatureConfigurationResult


class GuardDutyAccountFreeTrialInfo(BaseModel):
    AccountId: StrictStr | None = None
    DataSources: GuardDutyDataSourcesFreeTrial | None = None
    Features: list[GuardDutyFreeTrialFeatureConfigurationResult] | None = None
