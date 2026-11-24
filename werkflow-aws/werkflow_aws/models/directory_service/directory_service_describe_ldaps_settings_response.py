from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_ldaps_setting_info import DirectoryServiceLDAPSSettingInfo


class DirectoryServiceDescribeLDAPSSettingsResponse(BaseModel):
    LDAPSSettingsInfo: list[DirectoryServiceLDAPSSettingInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
