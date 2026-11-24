from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_detect_mitigation_actions_task_summary import IoTDetectMitigationActionsTaskSummary


class IoTListDetectMitigationActionsTasksResponse(BaseModel):
    tasks: list[IoTDetectMitigationActionsTaskSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
