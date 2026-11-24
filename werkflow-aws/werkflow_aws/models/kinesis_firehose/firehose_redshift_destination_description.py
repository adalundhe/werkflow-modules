from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_copy_command import FirehoseCopyCommand
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_redshift_retry_options import FirehoseRedshiftRetryOptions
from .firehose_s3_destination_description import FirehoseS3DestinationDescription
from .firehose_secrets_manager_configuration import FirehoseSecretsManagerConfiguration


class FirehoseRedshiftDestinationDescription(BaseModel):
    RoleARN: StrictStr | None = None
    ClusterJDBCURL: StrictStr | None = None
    CopyCommand: FirehoseCopyCommand | None = None
    Username: StrictStr | None = None
    RetryOptions: FirehoseRedshiftRetryOptions | None = None
    S3DestinationDescription: FirehoseS3DestinationDescription | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    S3BackupMode: StrictStr | None = None
    S3BackupDescription: FirehoseS3DestinationDescription | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    SecretsManagerConfiguration: FirehoseSecretsManagerConfiguration | None = None
