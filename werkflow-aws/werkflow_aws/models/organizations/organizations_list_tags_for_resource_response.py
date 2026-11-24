from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .organizations_tag import OrganizationsTag


class OrganizationsListTagsForResourceResponse(BaseModel):
    Tags: list[OrganizationsTag] | None = None
    NextToken: StrictStr | None = None
