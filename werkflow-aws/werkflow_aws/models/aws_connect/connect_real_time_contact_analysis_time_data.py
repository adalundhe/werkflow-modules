from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectRealTimeContactAnalysisTimeData(BaseModel):
    AbsoluteTime: datetime.datetime | StrictStr | None = None
