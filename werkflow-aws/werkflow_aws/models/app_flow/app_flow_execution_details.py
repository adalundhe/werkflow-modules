from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AppFlowExecutionDetails(BaseModel):
    mostRecentExecutionMessage: StrictStr | None = None
    mostRecentExecutionTime: datetime.datetime | StrictStr | None = None
    mostRecentExecutionStatus: StrictStr | None = None
