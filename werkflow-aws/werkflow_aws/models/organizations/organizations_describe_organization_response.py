from __future__ import annotations
from pydantic import BaseModel
from .organizations_organization import OrganizationsOrganization


class OrganizationsDescribeOrganizationResponse(BaseModel):
    Organization: OrganizationsOrganization | None = None
