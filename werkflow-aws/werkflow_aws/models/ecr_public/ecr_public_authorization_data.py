from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECRPublicAuthorizationData(BaseModel):
    authorizationToken: StrictStr | None = None
    expiresAt: datetime.datetime | StrictStr | None = None
