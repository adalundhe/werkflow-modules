from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WorkSpacesDescribeConnectClientAddInsRequest(BaseModel):
    ResourceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
