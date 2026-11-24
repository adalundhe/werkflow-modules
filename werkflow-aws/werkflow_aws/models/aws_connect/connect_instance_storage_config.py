from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_kinesis_firehose_config import ConnectKinesisFirehoseConfig
from .connect_kinesis_stream_config import ConnectKinesisStreamConfig
from .connect_kinesis_video_stream_config import ConnectKinesisVideoStreamConfig
from .connect_s3_config import ConnectS3Config


class ConnectInstanceStorageConfig(BaseModel):
    AssociationId: StrictStr | None = None
    StorageType: StrictStr | None = None
    S3Config: ConnectS3Config | None = None
    KinesisVideoStreamConfig: ConnectKinesisVideoStreamConfig | None = None
    KinesisStreamConfig: ConnectKinesisStreamConfig | None = None
    KinesisFirehoseConfig: ConnectKinesisFirehoseConfig | None = None
