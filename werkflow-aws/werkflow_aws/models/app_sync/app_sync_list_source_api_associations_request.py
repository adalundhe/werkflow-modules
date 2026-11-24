from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppSyncListSourceApiAssociationsRequest(BaseModel):
    apiId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
