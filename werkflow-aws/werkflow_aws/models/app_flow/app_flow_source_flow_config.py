from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_incremental_pull_config import AppFlowIncrementalPullConfig
from .app_flow_source_connector_properties import AppFlowSourceConnectorProperties


class AppFlowSourceFlowConfig(BaseModel):
    connectorType: StrictStr | None = None
    apiVersion: StrictStr | None = None
    connectorProfileName: StrictStr | None = None
    sourceConnectorProperties: AppFlowSourceConnectorProperties | None = None
    incrementalPullConfig: AppFlowIncrementalPullConfig | None = None
