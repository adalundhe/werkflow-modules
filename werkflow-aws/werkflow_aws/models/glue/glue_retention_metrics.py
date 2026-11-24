from __future__ import annotations
from pydantic import BaseModel
from .glue_iceberg_retention_metrics import GlueIcebergRetentionMetrics


class GlueRetentionMetrics(BaseModel):
    IcebergMetrics: GlueIcebergRetentionMetrics | None = None
