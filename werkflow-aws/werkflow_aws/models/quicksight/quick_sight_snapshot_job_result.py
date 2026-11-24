from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_anonymous_user_snapshot_job_result import QuickSightAnonymousUserSnapshotJobResult
from .quick_sight_registered_user_snapshot_job_result import QuickSightRegisteredUserSnapshotJobResult


class QuickSightSnapshotJobResult(BaseModel):
    AnonymousUsers: list[QuickSightAnonymousUserSnapshotJobResult] | None = None
    RegisteredUsers: list[QuickSightRegisteredUserSnapshotJobResult] | None = None
