from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class QuickSightWhatIfRangeScenario(BaseModel):
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    Value: StrictFloat | StrictInt | None = None
