from __future__ import annotations
from pydantic import BaseModel
from .transcribe_call_analytics_skipped_feature import TranscribeCallAnalyticsSkippedFeature


class TranscribeCallAnalyticsJobDetails(BaseModel):
    Skipped: list[TranscribeCallAnalyticsSkippedFeature] | None = None
