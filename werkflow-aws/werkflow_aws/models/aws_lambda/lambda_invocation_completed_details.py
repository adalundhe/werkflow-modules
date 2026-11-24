from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lambda_event_error import LambdaEventError


class LambdaInvocationCompletedDetails(BaseModel):
    StartTimestamp: datetime.datetime | StrictStr | None = None
    EndTimestamp: datetime.datetime | StrictStr | None = None
    RequestId: StrictStr | None = None
    Error: LambdaEventError | None = None
