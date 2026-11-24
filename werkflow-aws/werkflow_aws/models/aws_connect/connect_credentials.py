from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectCredentials(BaseModel):
    AccessToken: StrictStr | None = None
    AccessTokenExpiration: datetime.datetime | StrictStr | None = None
    RefreshToken: StrictStr | None = None
    RefreshTokenExpiration: datetime.datetime | StrictStr | None = None
