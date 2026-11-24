from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_destination_flow_config import AppFlowDestinationFlowConfig
from .app_flow_metadata_catalog_config import AppFlowMetadataCatalogConfig
from .app_flow_source_flow_config import AppFlowSourceFlowConfig
from .app_flow_task import AppFlowTask
from .app_flow_trigger_config import AppFlowTriggerConfig


class AppFlowUpdateFlowRequest(BaseModel):
    flowName: StrictStr
    triggerConfig: AppFlowTriggerConfig
    sourceFlowConfig: AppFlowSourceFlowConfig
    destinationFlowConfigList: list[AppFlowDestinationFlowConfig]
    tasks: list[AppFlowTask]
    description: StrictStr | None = None
    metadataCatalogConfig: AppFlowMetadataCatalogConfig | None = None
    clientToken: StrictStr | None = None
