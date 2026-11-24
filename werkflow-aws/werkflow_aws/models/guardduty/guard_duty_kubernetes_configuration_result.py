from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_kubernetes_audit_logs_configuration_result import GuardDutyKubernetesAuditLogsConfigurationResult


class GuardDutyKubernetesConfigurationResult(BaseModel):
    AuditLogs: GuardDutyKubernetesAuditLogsConfigurationResult | None = None
