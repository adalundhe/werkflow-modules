from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_real_time_contact_analysis_transcript_item_with_character_offsets import ConnectRealTimeContactAnalysisTranscriptItemWithCharacterOffsets


class ConnectRealTimeContactAnalysisExtractedInformationValue(BaseModel):
    Content: StrictStr | None = None
    PointsOfInterest: list[ConnectRealTimeContactAnalysisTranscriptItemWithCharacterOffsets] | None = None
