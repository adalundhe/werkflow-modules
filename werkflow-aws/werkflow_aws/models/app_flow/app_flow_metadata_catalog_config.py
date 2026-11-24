from __future__ import annotations
from pydantic import BaseModel
from .app_flow_glue_data_catalog_config import AppFlowGlueDataCatalogConfig


class AppFlowMetadataCatalogConfig(BaseModel):
    glueDataCatalog: AppFlowGlueDataCatalogConfig | None = None
