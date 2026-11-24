from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_malware_protection_configuration_result import GuardDutyMalwareProtectionConfigurationResult


class GuardDutyUnprocessedDataSourcesResult(BaseModel):
    MalwareProtection: GuardDutyMalwareProtectionConfigurationResult | None = None
