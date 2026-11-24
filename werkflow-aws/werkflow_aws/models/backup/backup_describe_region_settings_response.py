from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class BackupDescribeRegionSettingsResponse(BaseModel):
    ResourceTypeOptInPreference: dict[StrictStr, StrictBool] | None = None
    ResourceTypeManagementPreference: dict[StrictStr, StrictBool] | None = None
    ResourceTypeOptInIncremental: dict[StrictStr, StrictBool] | None = None
    ResponseMetadata: dict[str, Any] | None = None
