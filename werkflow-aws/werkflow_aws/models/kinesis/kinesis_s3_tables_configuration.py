from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_partition_spec import KinesisPartitionSpec


class KinesisS3TablesConfiguration(BaseModel):
    TableBucketARN: StrictStr | None = None
    Namespace: StrictStr | None = None
    TableName: StrictStr | None = None
    CompressionType: StrictStr | None = None
    PartitionSpec: KinesisPartitionSpec | None = None
