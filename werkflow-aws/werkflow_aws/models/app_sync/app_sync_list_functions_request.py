from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppSyncListFunctionsRequest(BaseModel):
    apiId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
