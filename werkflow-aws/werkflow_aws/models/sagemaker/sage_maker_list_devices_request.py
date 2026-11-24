from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListDevicesRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    LatestHeartbeatAfter: datetime.datetime | StrictStr | None = None
    ModelName: StrictStr | None = None
    DeviceFleetName: StrictStr | None = None
