from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_error_handling_config import AppFlowErrorHandlingConfig


class AppFlowSalesforceDestinationProperties(BaseModel):
    object: StrictStr | None = None
    idFieldNames: list[StrictStr] | None = None
    errorHandlingConfig: AppFlowErrorHandlingConfig | None = None
    writeOperationType: StrictStr | None = None
    dataTransferApi: StrictStr | None = None
