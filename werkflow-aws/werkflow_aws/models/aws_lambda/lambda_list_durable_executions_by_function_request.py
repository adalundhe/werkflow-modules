from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class LambdaListDurableExecutionsByFunctionRequest(BaseModel):
    FunctionName: StrictStr
    Qualifier: StrictStr | None = None
    DurableExecutionName: StrictStr | None = None
    Statuses: list[Literal['RUNNING', 'SUCCEEDED', 'FAILED', 'TIMED_OUT', 'STOPPED', 'DELETING', 'PAUSING', 'PAUSED']] | None = None
    StartedAfter: datetime.datetime | StrictStr | None = None
    StartedBefore: datetime.datetime | StrictStr | None = None
    ReverseOrder: StrictBool | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
