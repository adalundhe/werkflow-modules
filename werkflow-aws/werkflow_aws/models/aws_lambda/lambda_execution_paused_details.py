from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .lambda_event_pause_reason import LambdaEventPauseReason


class LambdaExecutionPausedDetails(BaseModel):
    PauseRequestTimestamp: datetime.datetime | StrictStr | None = None
    Reason: LambdaEventPauseReason | None = None
    ExecutionTimeoutPaused: StrictBool | None = None
