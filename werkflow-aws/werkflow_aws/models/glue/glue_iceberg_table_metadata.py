from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_iceberg_partition_spec import GlueIcebergPartitionSpec
from .glue_iceberg_schema import GlueIcebergSchema
from .glue_iceberg_sort_order import GlueIcebergSortOrder


class GlueIcebergTableMetadata(BaseModel):
    FormatVersion: StrictStr | None = None
    TableUuid: StrictStr | None = None
    Location: StrictStr | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
    Schemas: list[GlueIcebergSchema] | None = None
    CurrentSchemaId: StrictInt | None = None
    LastColumnId: StrictInt | None = None
    PartitionSpecs: list[GlueIcebergPartitionSpec] | None = None
    DefaultSpecId: StrictInt | None = None
    LastPartitionId: StrictInt | None = None
    SortOrders: list[GlueIcebergSortOrder] | None = None
    DefaultSortOrderId: StrictInt | None = None
