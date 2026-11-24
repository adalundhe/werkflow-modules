from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_session_tag import QuickSightSessionTag


class QuickSightSnapshotAnonymousUser(BaseModel):
    RowLevelPermissionTags: list[QuickSightSessionTag] | None = None
