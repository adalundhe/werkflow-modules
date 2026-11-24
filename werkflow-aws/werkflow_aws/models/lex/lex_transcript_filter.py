from __future__ import annotations
from pydantic import BaseModel
from .lex_transcript_filter_model import LexTranscriptFilterModel


class LexTranscriptFilter(BaseModel):
    lexTranscriptFilter: LexTranscriptFilterModel | None = None
