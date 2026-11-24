from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class GlueTaskRunFilterCriteria(BaseModel):
    TaskRunType: Literal['EVALUATION', 'LABELING_SET_GENERATION', 'IMPORT_LABELS', 'EXPORT_LABELS', 'FIND_MATCHES'] | None = None
    Status: Literal['STARTING', 'RUNNING', 'STOPPING', 'STOPPED', 'SUCCEEDED', 'FAILED', 'TIMEOUT'] | None = None
    StartedBefore: datetime.datetime | StrictStr | None = None
    StartedAfter: datetime.datetime | StrictStr | None = None
