from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ConnectEvaluationSuggestedAnswerTranscriptMillisecondOffsets(BaseModel):
    BeginOffsetMillis: StrictInt | None = None
