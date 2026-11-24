from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_assets_export_result import GlueAssetsExportResult
from .glue_s3_tables_configuration_result import GlueS3TablesConfigurationResult


class GlueGetDataCatalogExportConfigurationResponse(BaseModel):
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    S3TablesConfiguration: GlueS3TablesConfigurationResult | None = None
    Assets: GlueAssetsExportResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
