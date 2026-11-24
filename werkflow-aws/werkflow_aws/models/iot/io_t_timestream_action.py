from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_timestream_dimension import IoTTimestreamDimension
from .io_t_timestream_timestamp import IoTTimestreamTimestamp


class IoTTimestreamAction(BaseModel):
    roleArn: StrictStr | None = None
    databaseName: StrictStr | None = None
    tableName: StrictStr | None = None
    dimensions: list[IoTTimestreamDimension] | None = None
    timestamp: IoTTimestreamTimestamp | None = None
