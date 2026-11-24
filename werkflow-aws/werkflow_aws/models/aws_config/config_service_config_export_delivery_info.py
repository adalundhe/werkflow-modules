from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceConfigExportDeliveryInfo(BaseModel):
    lastStatus: StrictStr | None = None
    lastErrorCode: StrictStr | None = None
    lastErrorMessage: StrictStr | None = None
    lastAttemptTime: datetime.datetime | StrictStr | None = None
    lastSuccessfulTime: datetime.datetime | StrictStr | None = None
    nextDeliveryTime: datetime.datetime | StrictStr | None = None
