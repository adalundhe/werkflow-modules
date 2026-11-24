from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamWriteS3Configuration(BaseModel):
    BucketName: StrictStr | None = None
    ObjectKeyPrefix: StrictStr | None = None
    EncryptionOption: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
