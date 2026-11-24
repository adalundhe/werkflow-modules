from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKS3Storage(BaseModel):
    BucketArn: StrictStr | None = None
    CompressionType: StrictStr | None = None
    OutputPrefix: StrictStr | None = None
    OutputKeyTemplate: StrictStr | None = None
    StorageClass: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
