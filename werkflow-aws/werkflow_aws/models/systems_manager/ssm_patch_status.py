from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SSMPatchStatus(BaseModel):
    DeploymentStatus: StrictStr | None = None
    ComplianceLevel: StrictStr | None = None
    ApprovalDate: datetime.datetime | StrictStr | None = None
