from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BackupUpdateRegionSettingsRequest(BaseModel):
    ResourceTypeOptInPreference: dict[StrictStr, StrictBool] | None = None
    ResourceTypeManagementPreference: dict[StrictStr, StrictBool] | None = None
    ResourceTypeOptInIncremental: dict[StrictStr, StrictBool] | None = None
