from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DetectiveListMembersRequest(BaseModel):
    GraphArn: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
