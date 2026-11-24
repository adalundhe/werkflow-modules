from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_device_type import CognitoIDPDeviceType


class CognitoIDPAdminListDevicesResponse(BaseModel):
    Devices: list[CognitoIDPDeviceType] | None = None
    PaginationToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
