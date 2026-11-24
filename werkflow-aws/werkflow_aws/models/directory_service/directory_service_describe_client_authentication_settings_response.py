from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_client_authentication_setting_info import DirectoryServiceClientAuthenticationSettingInfo


class DirectoryServiceDescribeClientAuthenticationSettingsResponse(BaseModel):
    ClientAuthenticationSettingsInfo: list[DirectoryServiceClientAuthenticationSettingInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
