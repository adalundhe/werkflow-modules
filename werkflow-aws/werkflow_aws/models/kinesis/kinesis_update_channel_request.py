from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_channel_logging_update_input import KinesisChannelLoggingUpdateInput
from .kinesis_s3_destination_update_input import KinesisS3DestinationUpdateInput
from .kinesis_s3_tables_destination_update_input import KinesisS3TablesDestinationUpdateInput


class KinesisUpdateChannelRequest(BaseModel):
    ChannelARN: StrictStr
    S3DestinationConfiguration: KinesisS3DestinationUpdateInput | None = None
    S3TablesDestinationConfiguration: KinesisS3TablesDestinationUpdateInput | None = None
    LoggingConfiguration: KinesisChannelLoggingUpdateInput | None = None
