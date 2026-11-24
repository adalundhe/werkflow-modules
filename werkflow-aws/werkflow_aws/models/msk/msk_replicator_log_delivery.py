from __future__ import annotations
from pydantic import BaseModel
from .msk_replicator_cloud_watch_logs import MSKReplicatorCloudWatchLogs
from .msk_replicator_firehose import MSKReplicatorFirehose
from .msk_replicator_s3 import MSKReplicatorS3


class MSKReplicatorLogDelivery(BaseModel):
    CloudWatchLogs: MSKReplicatorCloudWatchLogs | None = None
    Firehose: MSKReplicatorFirehose | None = None
    S3: MSKReplicatorS3 | None = None
