from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_snapshot_anonymous_user import QuickSightSnapshotAnonymousUser


class QuickSightSnapshotUserConfiguration(BaseModel):
    AnonymousUsers: list[QuickSightSnapshotAnonymousUser] | None = None
