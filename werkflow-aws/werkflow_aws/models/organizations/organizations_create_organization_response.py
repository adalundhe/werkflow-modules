from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .organizations_organization_model import OrganizationsOrganizationModel


class OrganizationsCreateOrganizationResponse(BaseModel):
    Organization: OrganizationsOrganizationModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
