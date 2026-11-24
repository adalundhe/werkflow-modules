from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_error_handling_config import AppFlowErrorHandlingConfig


class AppFlowEventBridgeDestinationProperties(BaseModel):
    object: StrictStr | None = None
    errorHandlingConfig: AppFlowErrorHandlingConfig | None = None
