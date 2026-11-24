from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AmplifyGenerateAccessLogsRequest(BaseModel):
    domainName: StrictStr
    appId: StrictStr
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
