from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_remote_access_session import DeviceFarmRemoteAccessSession


class DeviceFarmListRemoteAccessSessionsResponse(BaseModel):
    remoteAccessSessions: list[DeviceFarmRemoteAccessSession] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
