from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .device_farm_create_remote_access_session_configuration import DeviceFarmCreateRemoteAccessSessionConfiguration


class DeviceFarmCreateRemoteAccessSessionRequest(BaseModel):
    projectArn: StrictStr
    deviceArn: StrictStr
    appArn: StrictStr | None = None
    instanceArn: StrictStr | None = None
    name: StrictStr | None = None
    configuration: DeviceFarmCreateRemoteAccessSessionConfiguration | None = None
    interactionMode: Literal['INTERACTIVE', 'NO_VIDEO', 'VIDEO_ONLY'] | None = None
    skipAppResign: StrictBool | None = None
