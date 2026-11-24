from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_processing_job_status import SageMakerProcessingJobStatus


class SageMakerProcessingJobSummary(BaseModel):
    ProcessingJobName: StrictStr | None = None
    ProcessingJobArn: StrictStr | None = None
    CreationTime: datetime.datetime | None = None
    ProcessingEndTime: datetime.datetime | None = None
    LastModifiedTime: datetime.datetime | None = None
    ProcessingJobStatus: SageMakerProcessingJobStatus | None = None
    FailureReason: StrictStr | None = None
    ExitMessage: StrictStr | None = None
