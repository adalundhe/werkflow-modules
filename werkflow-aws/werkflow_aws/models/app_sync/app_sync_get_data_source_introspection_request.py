from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AppSyncGetDataSourceIntrospectionRequest(BaseModel):
    introspectionId: StrictStr
    includeModelsSDL: StrictBool | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
