from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .kinesis_channel_encryption_configuration import KinesisChannelEncryptionConfiguration
from .kinesis_channel_logging_configuration import KinesisChannelLoggingConfiguration
from .kinesis_channel_stream_description import KinesisChannelStreamDescription
from .kinesis_s3_destination_description import KinesisS3DestinationDescription
from .kinesis_s3_tables_destination_description import KinesisS3TablesDestinationDescription


class KinesisChannelDescription(BaseModel):
    ChannelName: StrictStr | None = None
    ChannelARN: StrictStr | None = None
    ChannelId: StrictStr | None = None
    ChannelStatus: StrictStr | None = None
    ChannelStatusReason: StrictStr | None = None
    ChannelCreationTimestamp: datetime.datetime | StrictStr | None = None
    ServiceExecutionRoleARN: StrictStr | None = None
    StreamConfigurationList: list[KinesisChannelStreamDescription] | None = None
    S3DestinationConfiguration: KinesisS3DestinationDescription | None = None
    S3TablesDestinationConfiguration: KinesisS3TablesDestinationDescription | None = None
    EncryptionConfiguration: KinesisChannelEncryptionConfiguration | None = None
    LoggingConfiguration: KinesisChannelLoggingConfiguration | None = None
