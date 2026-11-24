from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexTestSetStorageLocation(BaseModel):
    s3BucketName: StrictStr | None = None
    s3Path: StrictStr | None = None
    kmsKeyArn: StrictStr | None = None
