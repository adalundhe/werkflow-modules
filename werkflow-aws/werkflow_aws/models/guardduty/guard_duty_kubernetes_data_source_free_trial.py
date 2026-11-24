from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_data_source_free_trial import GuardDutyDataSourceFreeTrial


class GuardDutyKubernetesDataSourceFreeTrial(BaseModel):
    AuditLogs: GuardDutyDataSourceFreeTrial | None = None
