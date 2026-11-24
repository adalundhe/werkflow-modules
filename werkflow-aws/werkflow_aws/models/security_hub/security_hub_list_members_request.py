from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SecurityHubListMembersRequest(BaseModel):
    OnlyAssociated: StrictBool | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
