from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IoTInfluxDBDestinationConfiguration(BaseModel):
    endpoint: StrictStr
    influxDBVersion: Literal['V2', 'V3']
    secretId: StrictStr
    secretType: Literal['SecretString', 'SecretBinary'] | None = None
    secretKey: StrictStr | None = None
