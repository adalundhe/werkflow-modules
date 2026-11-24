from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_iceberg_partition_spec import GlueIcebergPartitionSpec
from .glue_iceberg_schema import GlueIcebergSchema
from .glue_iceberg_sort_order import GlueIcebergSortOrder


class GlueCreateIcebergTableInput(BaseModel):
    Location: StrictStr
    Schema: GlueIcebergSchema
    PartitionSpec: GlueIcebergPartitionSpec | None = None
    WriteOrder: GlueIcebergSortOrder | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
