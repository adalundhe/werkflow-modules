from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IoTOTAUpdateSummary(BaseModel):
    otaUpdateId: StrictStr | None = None
    otaUpdateArn: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
