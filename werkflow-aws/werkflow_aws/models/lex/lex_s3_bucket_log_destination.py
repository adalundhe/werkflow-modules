from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexS3BucketLogDestination(BaseModel):
    kmsKeyArn: StrictStr | None = None
    s3BucketArn: StrictStr | None = None
    logPrefix: StrictStr | None = None
