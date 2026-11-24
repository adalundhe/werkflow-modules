from __future__ import annotations
from pydantic import BaseModel
from .connect_audio_quality_metrics_info import ConnectAudioQualityMetricsInfo


class ConnectCustomerQualityMetrics(BaseModel):
    Audio: ConnectAudioQualityMetricsInfo | None = None
