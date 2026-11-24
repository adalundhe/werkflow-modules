from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GlueSessionEndpoint(BaseModel):
    Url: StrictStr | None = None
    AuthToken: StrictStr | None = None
    AuthTokenExpirationTime: datetime.datetime | StrictStr | None = None
