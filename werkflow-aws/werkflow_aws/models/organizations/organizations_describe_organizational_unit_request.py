from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsDescribeOrganizationalUnitRequest(BaseModel):
    OrganizationalUnitId: StrictStr
