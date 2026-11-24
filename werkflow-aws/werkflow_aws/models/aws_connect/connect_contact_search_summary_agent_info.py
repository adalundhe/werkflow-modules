from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectContactSearchSummaryAgentInfo(BaseModel):
    Id: StrictStr | None = None
    ConnectedToAgentTimestamp: datetime.datetime | StrictStr | None = None
