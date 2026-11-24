from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_snapshot_operation_s3_prefix_location import KinesisAnalyticsSnapshotOperationS3PrefixLocation


class KinesisAnalyticsSnapshotOperationLocationDescription(BaseModel):
    LocationType: StrictStr | None = None
    S3PrefixLocation: KinesisAnalyticsSnapshotOperationS3PrefixLocation | None = None
