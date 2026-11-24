from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_real_time_contact_analysis_time_data import ConnectRealTimeContactAnalysisTimeData
from .connect_real_time_contact_analysis_transcript_item_redaction import ConnectRealTimeContactAnalysisTranscriptItemRedaction


class ConnectRealTimeContactAnalysisSegmentTranscript(BaseModel):
    Id: StrictStr | None = None
    ParticipantId: StrictStr | None = None
    ParticipantRole: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Content: StrictStr | None = None
    ContentType: StrictStr | None = None
    Time: ConnectRealTimeContactAnalysisTimeData | None = None
    Redaction: ConnectRealTimeContactAnalysisTranscriptItemRedaction | None = None
    Sentiment: StrictStr | None = None
