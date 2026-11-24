from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_snapshot_job_result_error_info import QuickSightSnapshotJobResultErrorInfo
from .quick_sight_snapshot_s3_destination_configuration import QuickSightSnapshotS3DestinationConfiguration


class QuickSightSnapshotJobS3Result(BaseModel):
    S3DestinationConfiguration: QuickSightSnapshotS3DestinationConfiguration | None = None
    S3Uri: StrictStr | None = None
    ErrorInfo: list[QuickSightSnapshotJobResultErrorInfo] | None = None
