from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .athena_error import AthenaError as _AthenaErrorType


class AthenaQueryExecutionStatus(BaseModel):
    State: StrictStr | None = None
    StateChangeReason: StrictStr | None = None
    SubmissionDateTime: datetime.datetime | StrictStr | None = None
    CompletionDateTime: datetime.datetime | StrictStr | None = None
    AthenaError: _AthenaErrorType | None = None
