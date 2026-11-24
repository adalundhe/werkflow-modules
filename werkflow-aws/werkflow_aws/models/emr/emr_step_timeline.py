from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EMRStepTimeline(BaseModel):
    CreationDateTime: datetime.datetime | StrictStr | None = None
    StartDateTime: datetime.datetime | StrictStr | None = None
    EndDateTime: datetime.datetime | StrictStr | None = None
