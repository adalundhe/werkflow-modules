from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieS3Destination(BaseModel):
    bucketName: StrictStr | None = None
    expectedBucketOwner: StrictStr | None = None
    keyPrefix: StrictStr | None = None
    kmsKeyArn: StrictStr | None = None
