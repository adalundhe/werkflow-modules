from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_error_handling_config import AppFlowErrorHandlingConfig


class AppFlowHoneycodeDestinationProperties(BaseModel):
    object: StrictStr | None = None
    errorHandlingConfig: AppFlowErrorHandlingConfig | None = None
