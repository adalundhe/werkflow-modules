from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECRAuthorizationData(BaseModel):
    authorizationToken: StrictStr | None = None
    expiresAt: datetime.datetime | StrictStr | None = None
    proxyEndpoint: StrictStr | None = None
