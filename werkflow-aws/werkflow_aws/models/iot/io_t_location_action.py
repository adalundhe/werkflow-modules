from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_location_timestamp import IoTLocationTimestamp


class IoTLocationAction(BaseModel):
    roleArn: StrictStr | None = None
    trackerName: StrictStr | None = None
    deviceId: StrictStr | None = None
    timestamp: IoTLocationTimestamp | None = None
    latitude: StrictStr | None = None
    longitude: StrictStr | None = None
