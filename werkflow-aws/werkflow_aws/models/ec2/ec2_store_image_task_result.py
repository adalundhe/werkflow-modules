from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EC2StoreImageTaskResult(BaseModel):
    AmiId: StrictStr | None = None
    TaskStartTime: datetime.datetime | StrictStr | None = None
    Bucket: StrictStr | None = None
    S3objectKey: StrictStr | None = None
    ProgressPercentage: StrictInt | None = None
    StoreTaskState: StrictStr | None = None
    StoreTaskFailureReason: StrictStr | None = None
