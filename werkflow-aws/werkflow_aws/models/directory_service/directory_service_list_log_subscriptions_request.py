from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectoryServiceListLogSubscriptionsRequest(BaseModel):
    DirectoryId: StrictStr | None = None
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
