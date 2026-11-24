from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSharePointParameters(BaseModel):
    SharePointDomain: StrictStr | None = None
    TenantId: StrictStr | None = None
    ClientId: StrictStr | None = None
    AuthType: StrictStr | None = None
