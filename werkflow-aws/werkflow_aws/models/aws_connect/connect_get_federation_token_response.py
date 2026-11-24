from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_credentials import ConnectCredentials


class ConnectGetFederationTokenResponse(BaseModel):
    UserId: StrictStr | None = None
    UserArn: StrictStr | None = None
    Credentials: ConnectCredentials | None = None
    SignInUrl: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
