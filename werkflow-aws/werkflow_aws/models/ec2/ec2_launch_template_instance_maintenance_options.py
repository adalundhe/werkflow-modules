from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2LaunchTemplateInstanceMaintenanceOptions(BaseModel):
    AutoRecovery: StrictStr | None = None
