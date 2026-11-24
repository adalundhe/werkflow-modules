from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class TranslateTextTranslationJobFilter(BaseModel):
    JobName: StrictStr | None = None
    JobStatus: Literal['SUBMITTED', 'IN_PROGRESS', 'COMPLETED', 'COMPLETED_WITH_ERROR', 'FAILED', 'STOP_REQUESTED', 'STOPPED'] | None = None
    SubmittedBeforeTime: datetime.datetime | StrictStr | None = None
    SubmittedAfterTime: datetime.datetime | StrictStr | None = None
