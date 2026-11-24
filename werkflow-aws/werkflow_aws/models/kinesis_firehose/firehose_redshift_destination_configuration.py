from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_copy_command import FirehoseCopyCommand
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_redshift_retry_options import FirehoseRedshiftRetryOptions
from .firehose_s3_destination_configuration import FirehoseS3DestinationConfiguration
from .firehose_secrets_manager_configuration import FirehoseSecretsManagerConfiguration


class FirehoseRedshiftDestinationConfiguration(BaseModel):
    RoleARN: StrictStr
    ClusterJDBCURL: StrictStr
    CopyCommand: FirehoseCopyCommand
    S3Configuration: FirehoseS3DestinationConfiguration
    Username: StrictStr | None = None
    Password: StrictStr | None = None
    RetryOptions: FirehoseRedshiftRetryOptions | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    S3BackupMode: Literal['Disabled', 'Enabled'] | None = None
    S3BackupConfiguration: FirehoseS3DestinationConfiguration | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    SecretsManagerConfiguration: FirehoseSecretsManagerConfiguration | None = None
