from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSnapshotAnonymousUserRedacted(BaseModel):
    RowLevelPermissionTagKeys: list[StrictStr] | None = None
