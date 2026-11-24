from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaWaitStartedDetails(BaseModel):
    Duration: StrictInt | None = None
    ScheduledEndTimestamp: datetime.datetime | StrictStr | None = None
