from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AmplifyListJobsRequest(BaseModel):
    appId: StrictStr
    branchName: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
