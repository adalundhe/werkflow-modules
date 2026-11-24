from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationStackSetAutoDeploymentTargetSummary(BaseModel):
    OrganizationalUnitId: StrictStr | None = None
    Regions: list[StrictStr] | None = None
