from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_sapo_data_pagination_config import AppFlowSAPODataPaginationConfig
from .app_flow_sapo_data_parallelism_config import AppFlowSAPODataParallelismConfig


class AppFlowSAPODataSourceProperties(BaseModel):
    objectPath: StrictStr | None = None
    parallelismConfig: AppFlowSAPODataParallelismConfig | None = None
    paginationConfig: AppFlowSAPODataPaginationConfig | None = None
