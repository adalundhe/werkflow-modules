from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_influx_db_batch_config import IoTInfluxDBBatchConfig


class IoTInfluxDBAction(BaseModel):
    destinationArn: StrictStr | None = None
    roleArn: StrictStr | None = None
    databaseName: StrictStr | None = None
    tableName: StrictStr | None = None
    organization: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    timestampUnit: StrictStr | None = None
    batchConfig: IoTInfluxDBBatchConfig | None = None
