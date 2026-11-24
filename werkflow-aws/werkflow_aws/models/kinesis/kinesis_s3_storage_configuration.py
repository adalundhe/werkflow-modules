from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisS3StorageConfiguration(BaseModel):
    BucketARN: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
    OutputKeyTemplate: StrictStr | None = None
    StorageClass: StrictStr | None = None
    CompressionType: StrictStr | None = None
