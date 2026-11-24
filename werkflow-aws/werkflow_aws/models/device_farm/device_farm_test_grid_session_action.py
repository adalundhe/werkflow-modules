from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class DeviceFarmTestGridSessionAction(BaseModel):
    action: StrictStr | None = None
    started: datetime.datetime | StrictStr | None = None
    duration: StrictInt | None = None
    statusCode: StrictStr | None = None
    requestMethod: StrictStr | None = None
