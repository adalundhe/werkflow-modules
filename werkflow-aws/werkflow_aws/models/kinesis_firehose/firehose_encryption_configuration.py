from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_kms_encryption_config import FirehoseKMSEncryptionConfig


class FirehoseEncryptionConfiguration(BaseModel):
    NoEncryptionConfig: StrictStr | None = None
    KMSEncryptionConfig: FirehoseKMSEncryptionConfig | None = None
