from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_auto_ml_partial_failure_reason import SageMakerAutoMLPartialFailureReason


class SageMakerAutoMLJobSummary(BaseModel):
    AutoMLJobName: StrictStr | None = None
    AutoMLJobArn: StrictStr | None = None
    AutoMLJobStatus: StrictStr | None = None
    AutoMLJobSecondaryStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    PartialFailureReasons: list[SageMakerAutoMLPartialFailureReason] | None = None
