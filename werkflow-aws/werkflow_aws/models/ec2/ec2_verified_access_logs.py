from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_verified_access_log_cloud_watch_logs_destination import EC2VerifiedAccessLogCloudWatchLogsDestination
from .ec2_verified_access_log_kinesis_data_firehose_destination import EC2VerifiedAccessLogKinesisDataFirehoseDestination
from .ec2_verified_access_log_s3_destination import EC2VerifiedAccessLogS3Destination


class EC2VerifiedAccessLogs(BaseModel):
    S3: EC2VerifiedAccessLogS3Destination | None = None
    CloudWatchLogs: EC2VerifiedAccessLogCloudWatchLogsDestination | None = None
    KinesisDataFirehose: EC2VerifiedAccessLogKinesisDataFirehoseDestination | None = None
    LogVersion: StrictStr | None = None
    IncludeTrustContext: StrictBool | None = None
