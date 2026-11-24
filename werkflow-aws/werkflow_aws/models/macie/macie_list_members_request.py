from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MacieListMembersRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    onlyAssociated: StrictStr | None = None
