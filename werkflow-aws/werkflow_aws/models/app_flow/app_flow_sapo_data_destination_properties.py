from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_error_handling_config import AppFlowErrorHandlingConfig
from .app_flow_success_response_handling_config import AppFlowSuccessResponseHandlingConfig


class AppFlowSAPODataDestinationProperties(BaseModel):
    objectPath: StrictStr | None = None
    successResponseHandlingConfig: AppFlowSuccessResponseHandlingConfig | None = None
    idFieldNames: list[StrictStr] | None = None
    errorHandlingConfig: AppFlowErrorHandlingConfig | None = None
    writeOperationType: StrictStr | None = None
