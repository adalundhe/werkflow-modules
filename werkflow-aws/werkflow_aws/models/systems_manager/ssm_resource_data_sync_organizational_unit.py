from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMResourceDataSyncOrganizationalUnit(BaseModel):
    OrganizationalUnitId: StrictStr | None = None
