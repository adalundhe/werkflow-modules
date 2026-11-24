from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_s3_tables_export_state import GlueS3TablesExportState


class GlueAssetsExportResult(BaseModel):
    S3TablesExport: StrictStr | None = None
    S3TablesExportState: GlueS3TablesExportState | None = None
