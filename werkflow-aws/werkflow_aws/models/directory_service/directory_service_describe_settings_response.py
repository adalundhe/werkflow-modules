from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_setting_entry import DirectoryServiceSettingEntry


class DirectoryServiceDescribeSettingsResponse(BaseModel):
    DirectoryId: StrictStr | None = None
    SettingEntries: list[DirectoryServiceSettingEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
