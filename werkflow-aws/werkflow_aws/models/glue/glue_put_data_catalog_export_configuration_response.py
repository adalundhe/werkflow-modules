from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_assets_export import GlueAssetsExport
from .glue_s3_tables_configuration import GlueS3TablesConfiguration


class GluePutDataCatalogExportConfigurationResponse(BaseModel):
    S3TablesConfiguration: GlueS3TablesConfiguration | None = None
    Assets: GlueAssetsExport | None = None
    ResponseMetadata: dict[str, Any] | None = None
