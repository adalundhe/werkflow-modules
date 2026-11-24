from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncDeleteApiKeyRequest(BaseModel):
    apiId: StrictStr
    id: StrictStr
