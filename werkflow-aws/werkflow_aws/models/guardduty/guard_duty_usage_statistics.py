from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_usage_account_result import GuardDutyUsageAccountResult
from .guard_duty_usage_data_source_result import GuardDutyUsageDataSourceResult
from .guard_duty_usage_feature_result import GuardDutyUsageFeatureResult
from .guard_duty_usage_resource_result import GuardDutyUsageResourceResult
from .guard_duty_usage_top_accounts_result import GuardDutyUsageTopAccountsResult


class GuardDutyUsageStatistics(BaseModel):
    SumByAccount: list[GuardDutyUsageAccountResult] | None = None
    TopAccountsByFeature: list[GuardDutyUsageTopAccountsResult] | None = None
    SumByDataSource: list[GuardDutyUsageDataSourceResult] | None = None
    SumByResource: list[GuardDutyUsageResourceResult] | None = None
    TopResources: list[GuardDutyUsageResourceResult] | None = None
    SumByFeature: list[GuardDutyUsageFeatureResult] | None = None
