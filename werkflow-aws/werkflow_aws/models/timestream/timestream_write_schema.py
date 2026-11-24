from __future__ import annotations
from pydantic import BaseModel
from .timestream_write_partition_key import TimestreamWritePartitionKey


class TimestreamWriteSchema(BaseModel):
    CompositePartitionKey: list[TimestreamWritePartitionKey] | None = None
