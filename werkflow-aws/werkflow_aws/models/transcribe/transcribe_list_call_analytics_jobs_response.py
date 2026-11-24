from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transcribe_call_analytics_job_summary import TranscribeCallAnalyticsJobSummary


class TranscribeListCallAnalyticsJobsResponse(BaseModel):
    Status: StrictStr | None = None
    NextToken: StrictStr | None = None
    CallAnalyticsJobSummaries: list[TranscribeCallAnalyticsJobSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
