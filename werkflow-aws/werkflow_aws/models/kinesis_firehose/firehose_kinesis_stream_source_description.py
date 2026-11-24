from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class FirehoseKinesisStreamSourceDescription(BaseModel):
    KinesisStreamARN: StrictStr | None = None
    RoleARN: StrictStr | None = None
    DeliveryStartTimestamp: datetime.datetime | StrictStr | None = None
