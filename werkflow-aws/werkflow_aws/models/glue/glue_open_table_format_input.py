from __future__ import annotations
from pydantic import BaseModel
from .glue_iceberg_input import GlueIcebergInput


class GlueOpenTableFormatInput(BaseModel):
    IcebergInput: GlueIcebergInput | None = None
