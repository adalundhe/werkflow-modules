from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupUpdateGlobalSettingsRequest(BaseModel):
    GlobalSettings: dict[StrictStr, StrictStr] | None = None
