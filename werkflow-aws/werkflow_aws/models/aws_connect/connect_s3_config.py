from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_encryption_config import ConnectEncryptionConfig


class ConnectS3Config(BaseModel):
    BucketName: StrictStr | None = None
    BucketPrefix: StrictStr | None = None
    EncryptionConfig: ConnectEncryptionConfig | None = None
