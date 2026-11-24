from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_authentication_profile import ConnectAuthenticationProfile


class ConnectDescribeAuthenticationProfileResponse(BaseModel):
    AuthenticationProfile: ConnectAuthenticationProfile | None = None
    ResponseMetadata: dict[str, Any] | None = None
