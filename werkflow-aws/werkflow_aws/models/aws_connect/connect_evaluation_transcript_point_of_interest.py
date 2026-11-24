from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_suggested_answer_transcript_millisecond_offsets import ConnectEvaluationSuggestedAnswerTranscriptMillisecondOffsets


class ConnectEvaluationTranscriptPointOfInterest(BaseModel):
    MillisecondOffsets: ConnectEvaluationSuggestedAnswerTranscriptMillisecondOffsets | None = None
    TranscriptSegment: StrictStr | None = None
