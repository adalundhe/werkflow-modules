from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .glue_catalog_table_config_options import GlueCatalogTableConfigOptions


class GlueDistributionResultsOptions(BaseModel):
    WriteDistributionResultsEnabled: StrictBool | None = None
    CatalogTableConfig: GlueCatalogTableConfigOptions | None = None
