from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsDeleteOrganizationalUnitRequest(BaseModel):
    OrganizationalUnitId: StrictStr
