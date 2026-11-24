from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_verified_access_log_cloud_watch_logs_destination_options import EC2VerifiedAccessLogCloudWatchLogsDestinationOptions
from .ec2_verified_access_log_kinesis_data_firehose_destination_options import EC2VerifiedAccessLogKinesisDataFirehoseDestinationOptions
from .ec2_verified_access_log_s3_destination_options import EC2VerifiedAccessLogS3DestinationOptions


class EC2VerifiedAccessLogOptions(BaseModel):
    S3: EC2VerifiedAccessLogS3DestinationOptions | None = None
    CloudWatchLogs: EC2VerifiedAccessLogCloudWatchLogsDestinationOptions | None = None
    KinesisDataFirehose: EC2VerifiedAccessLogKinesisDataFirehoseDestinationOptions | None = None
    LogVersion: StrictStr | None = None
    IncludeTrustContext: StrictBool | None = None
