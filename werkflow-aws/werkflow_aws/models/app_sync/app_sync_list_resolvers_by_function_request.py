from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppSyncListResolversByFunctionRequest(BaseModel):
    apiId: StrictStr
    functionId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
