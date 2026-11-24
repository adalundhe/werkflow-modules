from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_data_lake_access_properties_output import GlueDataLakeAccessPropertiesOutput
from .glue_iceberg_optimization_properties_output import GlueIcebergOptimizationPropertiesOutput


class GlueCatalogPropertiesOutput(BaseModel):
    DataLakeAccessProperties: GlueDataLakeAccessPropertiesOutput | None = None
    IcebergOptimizationProperties: GlueIcebergOptimizationPropertiesOutput | None = None
    CustomProperties: dict[StrictStr, StrictStr] | None = None
