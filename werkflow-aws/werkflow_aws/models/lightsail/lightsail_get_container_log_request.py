from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LightsailGetContainerLogRequest(BaseModel):
    serviceName: StrictStr
    containerName: StrictStr
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    filterPattern: StrictStr | None = None
    pageToken: StrictStr | None = None
