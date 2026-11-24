from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IoTBillingGroupMetadata(BaseModel):
    creationDate: datetime.datetime | StrictStr | None = None
