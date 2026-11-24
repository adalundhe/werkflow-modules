from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_auth_scope import ConnectAuthScope


class ConnectCreateAuthCodeRequest(BaseModel):
    InstanceId: StrictStr
    Scope: ConnectAuthScope
    SessionInactivityDurationMinutes: StrictInt
    MaxSessionDurationMinutes: StrictInt | None = None
