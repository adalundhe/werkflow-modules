from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .transcribe_absolute_time_range import TranscribeAbsoluteTimeRange
from .transcribe_relative_time_range import TranscribeRelativeTimeRange


class TranscribeSentimentFilter(BaseModel):
    Sentiments: list[StrictStr] | None = None
    AbsoluteTimeRange: TranscribeAbsoluteTimeRange | None = None
    RelativeTimeRange: TranscribeRelativeTimeRange | None = None
    ParticipantRole: StrictStr | None = None
    Negate: StrictBool | None = None
