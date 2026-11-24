from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_realtime_contact_analysis_segment import ConnectRealtimeContactAnalysisSegment


class ConnectListRealtimeContactAnalysisSegmentsV2Response(BaseModel):
    Channel: StrictStr | None = None
    Status: StrictStr | None = None
    Segments: list[ConnectRealtimeContactAnalysisSegment] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
