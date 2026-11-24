from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_partition_source import MSKPartitionSource


class MSKPartitionSpec(BaseModel):
    PartitionStrategy: StrictStr | None = None
    SourceList: list[MSKPartitionSource] | None = None
