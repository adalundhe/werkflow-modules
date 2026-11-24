from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_real_time_contact_analysis_character_interval import ConnectRealTimeContactAnalysisCharacterInterval


class ConnectRealTimeContactAnalysisTranscriptItemWithCharacterOffsets(BaseModel):
    Id: StrictStr | None = None
    CharacterOffsets: ConnectRealTimeContactAnalysisCharacterInterval | None = None
