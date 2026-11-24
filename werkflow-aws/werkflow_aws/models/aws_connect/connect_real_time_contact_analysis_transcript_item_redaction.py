from __future__ import annotations
from pydantic import BaseModel
from .connect_real_time_contact_analysis_character_interval import ConnectRealTimeContactAnalysisCharacterInterval


class ConnectRealTimeContactAnalysisTranscriptItemRedaction(BaseModel):
    CharacterOffsets: list[ConnectRealTimeContactAnalysisCharacterInterval] | None = None
