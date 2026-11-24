from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class LambdaPauseDetails(BaseModel):
    PauseRequestTimestamp: datetime.datetime | StrictStr | None = None
    Reason: StrictStr | None = None
    ExecutionTimeoutPaused: StrictBool | None = None
