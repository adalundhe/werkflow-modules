from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .transcribe_call_analytics_job_details import TranscribeCallAnalyticsJobDetails


class TranscribeCallAnalyticsJobSummary(BaseModel):
    CallAnalyticsJobName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    CompletionTime: datetime.datetime | StrictStr | None = None
    LanguageCode: StrictStr | None = None
    CallAnalyticsJobStatus: StrictStr | None = None
    CallAnalyticsJobDetails: TranscribeCallAnalyticsJobDetails | None = None
    FailureReason: StrictStr | None = None
