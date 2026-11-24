from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_real_time_contact_analysis_segments_filter import ConnectRealTimeContactAnalysisSegmentsFilter


class ConnectListRealtimeContactAnalysisSegmentsV2Request(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    OutputType: Literal['Raw', 'Redacted']
    SegmentTypes: list[Literal['Transcript', 'Categories', 'Issues', 'Event', 'Attachments', 'PostContactSummary', 'ExtractedInformation']]
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    ListFilter: ConnectRealTimeContactAnalysisSegmentsFilter | None = None
