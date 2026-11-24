from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDeadLetterQueueS3(BaseModel):
    BucketArn: StrictStr | None = None
    ErrorOutputPrefix: StrictStr | None = None
    ExpectedBucketOwner: StrictStr | None = None
