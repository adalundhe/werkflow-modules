from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EMRClusterTimeline(BaseModel):
    CreationDateTime: datetime.datetime | StrictStr | None = None
    ReadyDateTime: datetime.datetime | StrictStr | None = None
    EndDateTime: datetime.datetime | StrictStr | None = None
