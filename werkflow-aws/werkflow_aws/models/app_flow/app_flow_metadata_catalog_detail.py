from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_registration_output import AppFlowRegistrationOutput


class AppFlowMetadataCatalogDetail(BaseModel):
    catalogType: StrictStr | None = None
    tableName: StrictStr | None = None
    tableRegistrationOutput: AppFlowRegistrationOutput | None = None
    partitionRegistrationOutput: AppFlowRegistrationOutput | None = None
