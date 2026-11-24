from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .glue_iceberg_sort_field import GlueIcebergSortField


class GlueIcebergSortOrder(BaseModel):
    OrderId: StrictInt | None = None
    Fields: list[GlueIcebergSortField] | None = None
