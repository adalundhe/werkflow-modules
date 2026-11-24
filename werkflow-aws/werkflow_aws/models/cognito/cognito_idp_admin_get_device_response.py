from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_device_type import CognitoIDPDeviceType


class CognitoIDPAdminGetDeviceResponse(BaseModel):
    Device: CognitoIDPDeviceType | None = None
    ResponseMetadata: dict[str, Any] | None = None
