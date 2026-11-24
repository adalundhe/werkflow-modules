from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerDeviceFleetSummary(BaseModel):
    DeviceFleetArn: StrictStr | None = None
    DeviceFleetName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
