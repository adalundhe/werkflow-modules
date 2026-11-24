from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsUpdateOrganizationalUnitRequest(BaseModel):
    OrganizationalUnitId: StrictStr
    Name: StrictStr | None = None
