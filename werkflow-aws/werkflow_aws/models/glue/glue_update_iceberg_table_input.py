from __future__ import annotations
from pydantic import BaseModel
from .glue_iceberg_table_update import GlueIcebergTableUpdate


class GlueUpdateIcebergTableInput(BaseModel):
    Updates: list[GlueIcebergTableUpdate]
