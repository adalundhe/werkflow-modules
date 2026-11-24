from __future__ import annotations
from pydantic import BaseModel
from .awss3_continuation_event import AWSS3ContinuationEvent
from .awss3_end_event import AWSS3EndEvent
from .awss3_progress_event import AWSS3ProgressEvent
from .awss3_records_event import AWSS3RecordsEvent
from .awss3_stats_event import AWSS3StatsEvent


class AWSS3SelectObjectContentEventStream(BaseModel):
    Records: AWSS3RecordsEvent | None = None
    Stats: AWSS3StatsEvent | None = None
    Progress: AWSS3ProgressEvent | None = None
    Cont: AWSS3ContinuationEvent | None = None
    End: AWSS3EndEvent | None = None
