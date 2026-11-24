from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsListTagsForResourceRequest(BaseModel):
    ResourceId: StrictStr | None = None
    NextToken: StrictStr | None = None
