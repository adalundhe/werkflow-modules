from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_snapshot_job_result_file_group import QuickSightSnapshotJobResultFileGroup


class QuickSightAnonymousUserSnapshotJobResult(BaseModel):
    FileGroups: list[QuickSightSnapshotJobResultFileGroup] | None = None
