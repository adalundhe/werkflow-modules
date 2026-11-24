from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EMRStepExecutionStatusDetail(BaseModel):
    State: StrictStr | None = None
    CreationDateTime: datetime.datetime | StrictStr | None = None
    StartDateTime: datetime.datetime | StrictStr | None = None
    EndDateTime: datetime.datetime | StrictStr | None = None
    LastStateChangeReason: StrictStr | None = None
