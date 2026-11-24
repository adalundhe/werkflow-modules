from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceConfigStreamDeliveryInfo(BaseModel):
    lastStatus: StrictStr | None = None
    lastErrorCode: StrictStr | None = None
    lastErrorMessage: StrictStr | None = None
    lastStatusChangeTime: datetime.datetime | StrictStr | None = None
