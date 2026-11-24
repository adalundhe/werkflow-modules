from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightOneDriveParameters(BaseModel):
    TenantId: StrictStr | None = None
    ClientId: StrictStr | None = None
    AuthType: StrictStr | None = None
