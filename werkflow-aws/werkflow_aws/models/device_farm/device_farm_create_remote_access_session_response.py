from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_remote_access_session import DeviceFarmRemoteAccessSession


class DeviceFarmCreateRemoteAccessSessionResponse(BaseModel):
    remoteAccessSession: DeviceFarmRemoteAccessSession | None = None
    ResponseMetadata: dict[str, Any] | None = None
