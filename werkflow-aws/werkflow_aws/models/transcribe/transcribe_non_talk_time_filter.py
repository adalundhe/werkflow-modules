from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .transcribe_absolute_time_range import TranscribeAbsoluteTimeRange
from .transcribe_relative_time_range import TranscribeRelativeTimeRange


class TranscribeNonTalkTimeFilter(BaseModel):
    Threshold: StrictInt | None = None
    AbsoluteTimeRange: TranscribeAbsoluteTimeRange | None = None
    RelativeTimeRange: TranscribeRelativeTimeRange | None = None
    Negate: StrictBool | None = None
