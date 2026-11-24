from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .glue_iceberg_partition_field import GlueIcebergPartitionField


class GlueIcebergPartitionSpec(BaseModel):
    Fields: list[GlueIcebergPartitionField] | None = None
    SpecId: StrictInt | None = None
