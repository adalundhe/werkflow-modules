from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class DeviceFarmTestGridSession(BaseModel):
    arn: StrictStr | None = None
    status: StrictStr | None = None
    created: datetime.datetime | StrictStr | None = None
    ended: datetime.datetime | StrictStr | None = None
    billingMinutes: StrictFloat | StrictInt | None = None
    seleniumProperties: StrictStr | None = None
