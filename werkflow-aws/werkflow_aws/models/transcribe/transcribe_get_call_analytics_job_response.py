from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transcribe_call_analytics_job import TranscribeCallAnalyticsJob


class TranscribeGetCallAnalyticsJobResponse(BaseModel):
    CallAnalyticsJob: TranscribeCallAnalyticsJob | None = None
    ResponseMetadata: dict[str, Any] | None = None
