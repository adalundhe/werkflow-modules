from __future__ import annotations
from pydantic import BaseModel
from .glue_update_iceberg_table_input import GlueUpdateIcebergTableInput


class GlueUpdateIcebergInput(BaseModel):
    UpdateIcebergTableInput: GlueUpdateIcebergTableInput
