from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppSyncCreateApiKeyRequest(BaseModel):
    apiId: StrictStr
    description: StrictStr | None = None
    expires: StrictInt | None = None
