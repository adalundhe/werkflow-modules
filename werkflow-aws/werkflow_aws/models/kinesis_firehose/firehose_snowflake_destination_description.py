from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_s3_destination_description import FirehoseS3DestinationDescription
from .firehose_secrets_manager_configuration import FirehoseSecretsManagerConfiguration
from .firehose_snowflake_buffering_hints import FirehoseSnowflakeBufferingHints
from .firehose_snowflake_retry_options import FirehoseSnowflakeRetryOptions
from .firehose_snowflake_role_configuration import FirehoseSnowflakeRoleConfiguration
from .firehose_snowflake_vpc_configuration import FirehoseSnowflakeVpcConfiguration


class FirehoseSnowflakeDestinationDescription(BaseModel):
    AccountUrl: StrictStr | None = None
    User: StrictStr | None = None
    Database: StrictStr | None = None
    Schema: StrictStr | None = None
    Table: StrictStr | None = None
    SnowflakeRoleConfiguration: FirehoseSnowflakeRoleConfiguration | None = None
    DataLoadingOption: StrictStr | None = None
    MetaDataColumnName: StrictStr | None = None
    ContentColumnName: StrictStr | None = None
    SnowflakeVpcConfiguration: FirehoseSnowflakeVpcConfiguration | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    RoleARN: StrictStr | None = None
    RetryOptions: FirehoseSnowflakeRetryOptions | None = None
    S3BackupMode: StrictStr | None = None
    S3DestinationDescription: FirehoseS3DestinationDescription | None = None
    SecretsManagerConfiguration: FirehoseSecretsManagerConfiguration | None = None
    BufferingHints: FirehoseSnowflakeBufferingHints | None = None
