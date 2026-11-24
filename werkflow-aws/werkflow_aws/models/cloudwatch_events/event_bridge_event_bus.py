from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EventBridgeEventBus(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    Description: StrictStr | None = None
    Policy: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ManagedBy: StrictStr | None = None
