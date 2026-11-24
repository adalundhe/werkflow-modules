from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_assets_export import GlueAssetsExport
from .glue_s3_tables_configuration import GlueS3TablesConfiguration


class GluePutDataCatalogExportConfigurationRequest(BaseModel):
    ClientToken: StrictStr | None = None
    S3TablesConfiguration: GlueS3TablesConfiguration | None = None
    Assets: GlueAssetsExport | None = None
