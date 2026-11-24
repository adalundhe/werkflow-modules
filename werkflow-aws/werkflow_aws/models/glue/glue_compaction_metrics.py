from __future__ import annotations
from pydantic import BaseModel
from .glue_iceberg_compaction_metrics import GlueIcebergCompactionMetrics


class GlueCompactionMetrics(BaseModel):
    IcebergMetrics: GlueIcebergCompactionMetrics | None = None
