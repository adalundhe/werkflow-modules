from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppStreamDescribeEntitlementsRequest(BaseModel):
    StackName: StrictStr
    Name: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
