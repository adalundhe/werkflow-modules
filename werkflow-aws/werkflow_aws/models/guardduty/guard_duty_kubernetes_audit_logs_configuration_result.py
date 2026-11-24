from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyKubernetesAuditLogsConfigurationResult(BaseModel):
    Status: StrictStr | None = None
