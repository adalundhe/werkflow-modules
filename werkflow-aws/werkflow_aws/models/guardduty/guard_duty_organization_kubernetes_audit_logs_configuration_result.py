from __future__ import annotations
from pydantic import BaseModel, StrictBool


class GuardDutyOrganizationKubernetesAuditLogsConfigurationResult(BaseModel):
    AutoEnable: StrictBool | None = None
