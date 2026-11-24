from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisDeadLetterQueueS3Configuration(BaseModel):
    BucketARN: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
    ErrorOutputPrefix: StrictStr | None = None
