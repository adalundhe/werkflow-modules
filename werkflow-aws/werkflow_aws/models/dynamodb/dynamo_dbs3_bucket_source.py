from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBS3BucketSource(BaseModel):
    S3BucketOwner: StrictStr | None = None
    S3Bucket: StrictStr | None = None
    S3KeyPrefix: StrictStr | None = None
