from __future__ import annotations
from pydantic import BaseModel
from .glue_iceberg_compaction_configuration import GlueIcebergCompactionConfiguration


class GlueCompactionConfiguration(BaseModel):
    icebergConfiguration: GlueIcebergCompactionConfiguration | None = None
