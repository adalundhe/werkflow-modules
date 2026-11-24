from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lambda_event_resume_reason import LambdaEventResumeReason


class LambdaExecutionResumedDetails(BaseModel):
    ResumeRequestTimestamp: datetime.datetime | StrictStr | None = None
    Reason: LambdaEventResumeReason | None = None
