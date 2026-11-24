from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OrganizationsListParentsRequest(BaseModel):
    ChildId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
