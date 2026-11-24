from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_detect_mitigation_actions_task_summary import IoTDetectMitigationActionsTaskSummary


class IoTDescribeDetectMitigationActionsTaskResponse(BaseModel):
    taskSummary: IoTDetectMitigationActionsTaskSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
