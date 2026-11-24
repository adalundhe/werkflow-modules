from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .connect_transcript_criteria import ConnectTranscriptCriteria


class ConnectTranscript(BaseModel):
    Criteria: list[ConnectTranscriptCriteria]
    MatchType: Literal['MATCH_ALL', 'MATCH_ANY', 'MATCH_EXACT', 'MATCH_NONE'] | None = None
