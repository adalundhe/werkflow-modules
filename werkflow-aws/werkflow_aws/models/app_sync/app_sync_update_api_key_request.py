from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppSyncUpdateApiKeyRequest(BaseModel):
    apiId: StrictStr
    id: StrictStr
    description: StrictStr | None = None
    expires: StrictInt | None = None
