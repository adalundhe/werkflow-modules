from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTInfluxDBDestinationProperties(BaseModel):
    endpoint: StrictStr | None = None
    influxDBVersion: StrictStr | None = None
    secretId: StrictStr | None = None
    secretType: StrictStr | None = None
    secretKey: StrictStr | None = None
