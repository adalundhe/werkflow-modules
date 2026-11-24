from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_account_settings import DeviceFarmAccountSettings


class DeviceFarmGetAccountSettingsResponse(BaseModel):
    accountSettings: DeviceFarmAccountSettings | None = None
    ResponseMetadata: dict[str, Any] | None = None
