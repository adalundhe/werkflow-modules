from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_snapshot_file import QuickSightSnapshotFile
from .quick_sight_snapshot_job_s3_result import QuickSightSnapshotJobS3Result


class QuickSightSnapshotJobResultFileGroup(BaseModel):
    Files: list[QuickSightSnapshotFile] | None = None
    S3Results: list[QuickSightSnapshotJobS3Result] | None = None
