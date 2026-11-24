from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .organizations_organizational_unit import OrganizationsOrganizationalUnit


class OrganizationsListOrganizationalUnitsForParentResponse(BaseModel):
    OrganizationalUnits: list[OrganizationsOrganizationalUnit] | None = None
    NextToken: StrictStr | None = None
