from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_s3_destination_update import FirehoseS3DestinationUpdate
from .firehose_secrets_manager_configuration import FirehoseSecretsManagerConfiguration
from .firehose_snowflake_buffering_hints import FirehoseSnowflakeBufferingHints
from .firehose_snowflake_retry_options import FirehoseSnowflakeRetryOptions
from .firehose_snowflake_role_configuration import FirehoseSnowflakeRoleConfiguration


class FirehoseSnowflakeDestinationUpdate(BaseModel):
    AccountUrl: StrictStr | None = None
    PrivateKey: StrictStr | None = None
    KeyPassphrase: StrictStr | None = None
    User: StrictStr | None = None
    Database: StrictStr | None = None
    Schema: StrictStr | None = None
    Table: StrictStr | None = None
    SnowflakeRoleConfiguration: FirehoseSnowflakeRoleConfiguration | None = None
    DataLoadingOption: Literal['JSON_MAPPING', 'VARIANT_CONTENT_MAPPING', 'VARIANT_CONTENT_AND_METADATA_MAPPING'] | None = None
    MetaDataColumnName: StrictStr | None = None
    ContentColumnName: StrictStr | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    RoleARN: StrictStr | None = None
    RetryOptions: FirehoseSnowflakeRetryOptions | None = None
    S3BackupMode: Literal['FailedDataOnly', 'AllData'] | None = None
    S3Update: FirehoseS3DestinationUpdate | None = None
    SecretsManagerConfiguration: FirehoseSecretsManagerConfiguration | None = None
    BufferingHints: FirehoseSnowflakeBufferingHints | None = None
