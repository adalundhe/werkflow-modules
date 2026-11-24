from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_snapshot_anonymous_user_redacted import QuickSightSnapshotAnonymousUserRedacted


class QuickSightSnapshotUserConfigurationRedacted(BaseModel):
    AnonymousUsers: list[QuickSightSnapshotAnonymousUserRedacted] | None = None
