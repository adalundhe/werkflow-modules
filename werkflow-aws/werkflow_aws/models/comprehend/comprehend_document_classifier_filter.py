from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComprehendDocumentClassifierFilter(BaseModel):
    Status: Literal['SUBMITTED', 'TRAINING', 'DELETING', 'STOP_REQUESTED', 'STOPPED', 'IN_ERROR', 'TRAINED', 'TRAINED_WITH_WARNING'] | None = None
    DocumentClassifierName: StrictStr | None = None
    SubmitTimeBefore: datetime.datetime | StrictStr | None = None
    SubmitTimeAfter: datetime.datetime | StrictStr | None = None
