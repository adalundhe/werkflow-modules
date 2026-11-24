from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class FMSListAppsListsRequest(BaseModel):
    MaxResults: StrictInt
    DefaultLists: StrictBool | None = None
    NextToken: StrictStr | None = None
