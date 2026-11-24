from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class QuickSightWhatIfPointScenario(BaseModel):
    Date: datetime.datetime | StrictStr | None = None
    Value: StrictFloat | StrictInt | None = None
