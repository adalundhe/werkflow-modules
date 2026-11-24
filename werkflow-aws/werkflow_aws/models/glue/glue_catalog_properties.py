from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_data_lake_access_properties import GlueDataLakeAccessProperties
from .glue_iceberg_optimization_properties import GlueIcebergOptimizationProperties


class GlueCatalogProperties(BaseModel):
    DataLakeAccessProperties: GlueDataLakeAccessProperties | None = None
    IcebergOptimizationProperties: GlueIcebergOptimizationProperties | None = None
    CustomProperties: dict[StrictStr, StrictStr] | None = None
