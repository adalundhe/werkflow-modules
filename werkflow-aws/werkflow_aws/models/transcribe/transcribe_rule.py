from __future__ import annotations
from pydantic import BaseModel
from .transcribe_interruption_filter import TranscribeInterruptionFilter
from .transcribe_non_talk_time_filter import TranscribeNonTalkTimeFilter
from .transcribe_sentiment_filter import TranscribeSentimentFilter
from .transcribe_transcript_filter import TranscribeTranscriptFilter


class TranscribeRule(BaseModel):
    NonTalkTimeFilter: TranscribeNonTalkTimeFilter | None = None
    InterruptionFilter: TranscribeInterruptionFilter | None = None
    TranscriptFilter: TranscribeTranscriptFilter | None = None
    SentimentFilter: TranscribeSentimentFilter | None = None
