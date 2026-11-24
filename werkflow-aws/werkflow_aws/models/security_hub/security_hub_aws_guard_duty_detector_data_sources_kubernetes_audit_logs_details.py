from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetails(BaseModel):
    Status: StrictStr | None = None
