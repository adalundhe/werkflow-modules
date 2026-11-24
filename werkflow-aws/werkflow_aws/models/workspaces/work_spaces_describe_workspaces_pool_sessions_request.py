from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WorkSpacesDescribeWorkspacesPoolSessionsRequest(BaseModel):
    PoolId: StrictStr
    UserId: StrictStr | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
