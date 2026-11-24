from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .app_flow_destination_flow_config import AppFlowDestinationFlowConfig
from .app_flow_execution_details import AppFlowExecutionDetails
from .app_flow_metadata_catalog_config import AppFlowMetadataCatalogConfig
from .app_flow_metadata_catalog_detail import AppFlowMetadataCatalogDetail
from .app_flow_source_flow_config import AppFlowSourceFlowConfig
from .app_flow_task import AppFlowTask
from .app_flow_trigger_config import AppFlowTriggerConfig


class AppFlowDescribeFlowResponse(BaseModel):
    flowArn: StrictStr | None = None
    description: StrictStr | None = None
    flowName: StrictStr | None = None
    kmsArn: StrictStr | None = None
    flowStatus: StrictStr | None = None
    flowStatusMessage: StrictStr | None = None
    sourceFlowConfig: AppFlowSourceFlowConfig | None = None
    destinationFlowConfigList: list[AppFlowDestinationFlowConfig] | None = None
    lastRunExecutionDetails: AppFlowExecutionDetails | None = None
    triggerConfig: AppFlowTriggerConfig | None = None
    tasks: list[AppFlowTask] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    lastUpdatedBy: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    metadataCatalogConfig: AppFlowMetadataCatalogConfig | None = None
    lastRunMetadataCatalogDetails: list[AppFlowMetadataCatalogDetail] | None = None
    schemaVersion: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
