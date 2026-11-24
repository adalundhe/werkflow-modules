from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .organizations_parent import OrganizationsParent


class OrganizationsListParentsResponse(BaseModel):
    Parents: list[OrganizationsParent] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
