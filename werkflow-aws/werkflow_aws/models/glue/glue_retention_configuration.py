from __future__ import annotations
from pydantic import BaseModel
from .glue_iceberg_retention_configuration import GlueIcebergRetentionConfiguration


class GlueRetentionConfiguration(BaseModel):
    icebergConfiguration: GlueIcebergRetentionConfiguration | None = None
