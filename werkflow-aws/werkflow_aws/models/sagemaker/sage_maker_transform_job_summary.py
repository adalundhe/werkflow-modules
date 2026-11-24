from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerTransformJobSummary(BaseModel):
    TransformJobName: StrictStr | None = None
    TransformJobArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    TransformEndTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    TransformJobStatus: StrictStr | None = None
    FailureReason: StrictStr | None = None
