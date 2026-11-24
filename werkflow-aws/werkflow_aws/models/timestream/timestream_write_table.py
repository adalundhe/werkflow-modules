from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .timestream_write_magnetic_store_write_properties import TimestreamWriteMagneticStoreWriteProperties
from .timestream_write_retention_properties import TimestreamWriteRetentionProperties
from .timestream_write_schema import TimestreamWriteSchema


class TimestreamWriteTable(BaseModel):
    Arn: StrictStr | None = None
    TableName: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    TableStatus: StrictStr | None = None
    RetentionProperties: TimestreamWriteRetentionProperties | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    MagneticStoreWriteProperties: TimestreamWriteMagneticStoreWriteProperties | None = None
    Schema: TimestreamWriteSchema | None = None
