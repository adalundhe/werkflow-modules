from __future__ import annotations
from pydantic import BaseModel, StrictBool


class GuardDutyOrganizationKubernetesAuditLogsConfiguration(BaseModel):
    AutoEnable: StrictBool
