from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_connector_operator import AppFlowConnectorOperator


class AppFlowTask(BaseModel):
    sourceFields: list[StrictStr] | None = None
    connectorOperator: AppFlowConnectorOperator | None = None
    destinationField: StrictStr | None = None
    taskType: StrictStr | None = None
    taskProperties: dict[StrictStr, StrictStr] | None = None
