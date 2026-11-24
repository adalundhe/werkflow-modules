from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_detect_mitigation_action_execution import IoTDetectMitigationActionExecution


class IoTListDetectMitigationActionsExecutionsResponse(BaseModel):
    actionsExecutions: list[IoTDetectMitigationActionExecution] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
