from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_video_stream_storage_configuration import KinesisVideoStreamStorageConfiguration


class KinesisVideoCreateStreamRequest(BaseModel):
    StreamName: StrictStr
    DeviceName: StrictStr | None = None
    MediaType: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    DataRetentionInHours: StrictInt | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    StreamStorageConfiguration: KinesisVideoStreamStorageConfiguration | None = None
