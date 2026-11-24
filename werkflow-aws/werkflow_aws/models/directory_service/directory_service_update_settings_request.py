from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .directory_service_setting import DirectoryServiceSetting


class DirectoryServiceUpdateSettingsRequest(BaseModel):
    DirectoryId: StrictStr
    Settings: list[DirectoryServiceSetting]
