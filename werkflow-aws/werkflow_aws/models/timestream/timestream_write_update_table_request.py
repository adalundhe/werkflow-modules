from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_write_magnetic_store_write_properties import TimestreamWriteMagneticStoreWriteProperties
from .timestream_write_retention_properties import TimestreamWriteRetentionProperties
from .timestream_write_schema import TimestreamWriteSchema


class TimestreamWriteUpdateTableRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    RetentionProperties: TimestreamWriteRetentionProperties | None = None
    MagneticStoreWriteProperties: TimestreamWriteMagneticStoreWriteProperties | None = None
    Schema: TimestreamWriteSchema | None = None
