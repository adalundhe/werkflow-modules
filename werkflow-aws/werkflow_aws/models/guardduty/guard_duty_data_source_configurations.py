from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_kubernetes_configuration import GuardDutyKubernetesConfiguration
from .guard_duty_malware_protection_configuration import GuardDutyMalwareProtectionConfiguration
from .guard_duty_s3_logs_configuration import GuardDutyS3LogsConfiguration


class GuardDutyDataSourceConfigurations(BaseModel):
    S3Logs: GuardDutyS3LogsConfiguration | None = None
    Kubernetes: GuardDutyKubernetesConfiguration | None = None
    MalwareProtection: GuardDutyMalwareProtectionConfiguration | None = None
