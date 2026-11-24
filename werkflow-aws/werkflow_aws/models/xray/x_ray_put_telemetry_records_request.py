from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .x_ray_telemetry_record import XRayTelemetryRecord


class XRayPutTelemetryRecordsRequest(BaseModel):
    TelemetryRecords: list[XRayTelemetryRecord]
    EC2InstanceId: StrictStr | None = None
    Hostname: StrictStr | None = None
    ResourceARN: StrictStr | None = None
