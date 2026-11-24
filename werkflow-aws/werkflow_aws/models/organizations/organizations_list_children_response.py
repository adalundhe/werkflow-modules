from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .organizations_child import OrganizationsChild


class OrganizationsListChildrenResponse(BaseModel):
    Children: list[OrganizationsChild] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
