from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DMSSourceDataSetting(BaseModel):
    CDCStartPosition: StrictStr | None = None
    CDCStartTime: datetime.datetime | StrictStr | None = None
    CDCStopTime: datetime.datetime | StrictStr | None = None
    SlotName: StrictStr | None = None
