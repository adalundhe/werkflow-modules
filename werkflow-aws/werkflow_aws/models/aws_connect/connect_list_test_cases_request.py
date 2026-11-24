from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListTestCasesRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
