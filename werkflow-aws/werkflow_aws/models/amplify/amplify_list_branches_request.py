from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AmplifyListBranchesRequest(BaseModel):
    appId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
