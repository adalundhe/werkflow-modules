from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .app_flow_aggregation_config import AppFlowAggregationConfig
from .app_flow_prefix_config import AppFlowPrefixConfig


class AppFlowS3OutputFormatConfig(BaseModel):
    fileType: StrictStr | None = None
    prefixConfig: AppFlowPrefixConfig | None = None
    aggregationConfig: AppFlowAggregationConfig | None = None
    preserveSourceDataTyping: StrictBool | None = None
