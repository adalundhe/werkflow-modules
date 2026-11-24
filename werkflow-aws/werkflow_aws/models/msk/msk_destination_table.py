from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_partition_spec import MSKPartitionSpec


class MSKDestinationTable(BaseModel):
    DestinationDatabaseName: StrictStr | None = None
    DestinationTableName: StrictStr | None = None
    PartitionSpec: MSKPartitionSpec | None = None
