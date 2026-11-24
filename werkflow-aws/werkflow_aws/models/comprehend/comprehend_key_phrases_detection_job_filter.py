from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComprehendKeyPhrasesDetectionJobFilter(BaseModel):
    JobName: StrictStr | None = None
    JobStatus: Literal['SUBMITTED', 'IN_PROGRESS', 'COMPLETED', 'FAILED', 'STOP_REQUESTED', 'STOPPED'] | None = None
    SubmitTimeBefore: datetime.datetime | StrictStr | None = None
    SubmitTimeAfter: datetime.datetime | StrictStr | None = None
