from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class IAMGetMFADeviceResponse(BaseModel):
    UserName: StrictStr | None = None
    SerialNumber: StrictStr | None = None
    EnableDate: datetime.datetime | StrictStr | None = None
    Certifications: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
