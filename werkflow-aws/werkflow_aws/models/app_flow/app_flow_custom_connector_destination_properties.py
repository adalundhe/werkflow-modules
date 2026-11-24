from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_error_handling_config import AppFlowErrorHandlingConfig


class AppFlowCustomConnectorDestinationProperties(BaseModel):
    entityName: StrictStr | None = None
    errorHandlingConfig: AppFlowErrorHandlingConfig | None = None
    writeOperationType: StrictStr | None = None
    idFieldNames: list[StrictStr] | None = None
    customProperties: dict[StrictStr, StrictStr] | None = None
