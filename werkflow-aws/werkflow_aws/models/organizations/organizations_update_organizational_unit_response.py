from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .organizations_organizational_unit_model import OrganizationsOrganizationalUnitModel


class OrganizationsUpdateOrganizationalUnitResponse(BaseModel):
    OrganizationalUnit: OrganizationsOrganizationalUnitModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
