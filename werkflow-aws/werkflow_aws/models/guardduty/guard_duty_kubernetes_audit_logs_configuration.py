from __future__ import annotations
from pydantic import BaseModel, StrictBool


class GuardDutyKubernetesAuditLogsConfiguration(BaseModel):
    Enable: StrictBool
