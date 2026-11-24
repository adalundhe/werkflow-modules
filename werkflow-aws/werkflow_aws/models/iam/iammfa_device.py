from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IAMMFADevice(BaseModel):
    UserName: StrictStr | None = None
    SerialNumber: StrictStr | None = None
    EnableDate: datetime.datetime | StrictStr | None = None
