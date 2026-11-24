from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_catalog_table_config_options import GlueCatalogTableConfigOptions


class GlueRowLevelResultsOptions(BaseModel):
    MaxRowsToWrite: StrictInt | None = None
    ResultType: StrictStr | None = None
    CatalogTableConfig: GlueCatalogTableConfigOptions | None = None
