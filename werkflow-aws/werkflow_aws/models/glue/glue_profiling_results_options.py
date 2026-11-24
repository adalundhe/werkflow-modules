from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .glue_catalog_table_config_options import GlueCatalogTableConfigOptions
from .glue_distribution_results_options import GlueDistributionResultsOptions


class GlueProfilingResultsOptions(BaseModel):
    WriteProfilingResultsEnabled: StrictBool | None = None
    CatalogTableConfig: GlueCatalogTableConfigOptions | None = None
    DistributionResults: GlueDistributionResultsOptions | None = None
