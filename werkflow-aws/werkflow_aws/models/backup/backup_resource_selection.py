from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BackupResourceSelection(BaseModel):
    Resources: list[StrictStr] | None = None
    TieringDownSettingsInDays: StrictInt | None = None
    ResourceType: StrictStr | None = None
