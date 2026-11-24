from __future__ import annotations
from pydantic import BaseModel
from .glue_iceberg_orphan_file_deletion_configuration import GlueIcebergOrphanFileDeletionConfiguration


class GlueOrphanFileDeletionConfiguration(BaseModel):
    icebergConfiguration: GlueIcebergOrphanFileDeletionConfiguration | None = None
