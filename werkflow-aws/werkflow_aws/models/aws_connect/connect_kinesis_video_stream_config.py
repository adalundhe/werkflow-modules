from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_encryption_config import ConnectEncryptionConfig


class ConnectKinesisVideoStreamConfig(BaseModel):
    Prefix: StrictStr | None = None
    RetentionPeriodHours: StrictInt | None = None
    EncryptionConfig: ConnectEncryptionConfig | None = None
