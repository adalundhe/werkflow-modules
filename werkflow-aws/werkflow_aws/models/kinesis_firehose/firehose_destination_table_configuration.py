from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_partition_spec import FirehosePartitionSpec


class FirehoseDestinationTableConfiguration(BaseModel):
    DestinationTableName: StrictStr | None = None
    DestinationDatabaseName: StrictStr | None = None
    UniqueKeys: list[StrictStr] | None = None
    PartitionSpec: FirehosePartitionSpec | None = None
    S3ErrorOutputPrefix: StrictStr | None = None
