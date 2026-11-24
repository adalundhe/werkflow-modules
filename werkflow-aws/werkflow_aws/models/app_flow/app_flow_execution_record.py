from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .app_flow_execution_result import AppFlowExecutionResult
from .app_flow_metadata_catalog_detail import AppFlowMetadataCatalogDetail


class AppFlowExecutionRecord(BaseModel):
    executionId: StrictStr | None = None
    executionStatus: StrictStr | None = None
    executionResult: AppFlowExecutionResult | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    dataPullStartTime: datetime.datetime | StrictStr | None = None
    dataPullEndTime: datetime.datetime | StrictStr | None = None
    metadataCatalogDetails: list[AppFlowMetadataCatalogDetail] | None = None
