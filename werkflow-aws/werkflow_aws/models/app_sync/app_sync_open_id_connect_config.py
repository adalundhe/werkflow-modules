from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppSyncOpenIDConnectConfig(BaseModel):
    issuer: StrictStr | None = None
    clientId: StrictStr | None = None
    iatTTL: StrictInt | None = None
    authTTL: StrictInt | None = None
