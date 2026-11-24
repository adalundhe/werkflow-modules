from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_data_source_free_trial import GuardDutyDataSourceFreeTrial
from .guard_duty_kubernetes_data_source_free_trial import GuardDutyKubernetesDataSourceFreeTrial
from .guard_duty_malware_protection_data_source_free_trial import GuardDutyMalwareProtectionDataSourceFreeTrial


class GuardDutyDataSourcesFreeTrial(BaseModel):
    CloudTrail: GuardDutyDataSourceFreeTrial | None = None
    DnsLogs: GuardDutyDataSourceFreeTrial | None = None
    FlowLogs: GuardDutyDataSourceFreeTrial | None = None
    S3Logs: GuardDutyDataSourceFreeTrial | None = None
    Kubernetes: GuardDutyKubernetesDataSourceFreeTrial | None = None
    MalwareProtection: GuardDutyMalwareProtectionDataSourceFreeTrial | None = None
