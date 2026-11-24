from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_real_time_contact_analysis_attachment import ConnectRealTimeContactAnalysisAttachment
from .connect_real_time_contact_analysis_time_data import ConnectRealTimeContactAnalysisTimeData


class ConnectRealTimeContactAnalysisSegmentAttachments(BaseModel):
    Id: StrictStr | None = None
    ParticipantId: StrictStr | None = None
    ParticipantRole: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Attachments: list[ConnectRealTimeContactAnalysisAttachment] | None = None
    Time: ConnectRealTimeContactAnalysisTimeData | None = None
