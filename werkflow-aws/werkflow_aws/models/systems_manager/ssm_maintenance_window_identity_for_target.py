from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMMaintenanceWindowIdentityForTarget(BaseModel):
    WindowId: StrictStr | None = None
    Name: StrictStr | None = None
