from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_channel_encryption_configuration import KinesisChannelEncryptionConfiguration
from .kinesis_channel_logging_configuration import KinesisChannelLoggingConfiguration
from .kinesis_channel_stream_configuration import KinesisChannelStreamConfiguration
from .kinesis_s3_destination_configuration import KinesisS3DestinationConfiguration
from .kinesis_s3_tables_destination_configuration import KinesisS3TablesDestinationConfiguration


class KinesisCreateChannelRequest(BaseModel):
    ChannelName: StrictStr
    ServiceExecutionRoleARN: StrictStr
    StreamConfigurationList: list[KinesisChannelStreamConfiguration]
    S3DestinationConfiguration: KinesisS3DestinationConfiguration | None = None
    S3TablesDestinationConfiguration: KinesisS3TablesDestinationConfiguration | None = None
    EncryptionConfiguration: KinesisChannelEncryptionConfiguration | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    LoggingConfiguration: KinesisChannelLoggingConfiguration | None = None
