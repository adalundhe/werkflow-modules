from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .app_flow_execution_details import AppFlowExecutionDetails


class AppFlowFlowDefinition(BaseModel):
    flowArn: StrictStr | None = None
    description: StrictStr | None = None
    flowName: StrictStr | None = None
    flowStatus: StrictStr | None = None
    sourceConnectorType: StrictStr | None = None
    sourceConnectorLabel: StrictStr | None = None
    destinationConnectorType: StrictStr | None = None
    destinationConnectorLabel: StrictStr | None = None
    triggerType: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    lastUpdatedBy: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    lastRunExecutionDetails: AppFlowExecutionDetails | None = None
