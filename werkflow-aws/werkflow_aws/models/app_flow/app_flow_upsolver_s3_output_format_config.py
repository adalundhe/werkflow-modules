from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_aggregation_config import AppFlowAggregationConfig
from .app_flow_prefix_config import AppFlowPrefixConfig


class AppFlowUpsolverS3OutputFormatConfig(BaseModel):
    fileType: StrictStr | None = None
    prefixConfig: AppFlowPrefixConfig | None = None
    aggregationConfig: AppFlowAggregationConfig | None = None
