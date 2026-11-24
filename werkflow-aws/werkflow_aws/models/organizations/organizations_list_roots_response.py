from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .organizations_root import OrganizationsRoot


class OrganizationsListRootsResponse(BaseModel):
    Roots: list[OrganizationsRoot] | None = None
    NextToken: StrictStr | None = None
