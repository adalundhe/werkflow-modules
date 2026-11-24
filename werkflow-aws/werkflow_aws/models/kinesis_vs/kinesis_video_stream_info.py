from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisVideoStreamInfo(BaseModel):
    DeviceName: StrictStr | None = None
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    MediaType: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    Version: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    DataRetentionInHours: StrictInt | None = None
