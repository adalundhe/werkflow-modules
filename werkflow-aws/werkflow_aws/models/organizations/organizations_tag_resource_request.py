from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .organizations_tag import OrganizationsTag


class OrganizationsTagResourceRequest(BaseModel):
    ResourceId: StrictStr | None = None
    Tags: list[OrganizationsTag] | None = None
