from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_detect_mitigation_actions_task_target import IoTDetectMitigationActionsTaskTarget
from .io_t_violation_event_occurrence_range import IoTViolationEventOccurrenceRange


class IoTStartDetectMitigationActionsTaskRequest(BaseModel):
    taskId: StrictStr
    target: IoTDetectMitigationActionsTaskTarget
    actions: list[StrictStr]
    clientRequestToken: StrictStr
    violationEventOccurrenceRange: IoTViolationEventOccurrenceRange | None = None
    includeOnlyActiveViolations: StrictBool | None = None
    includeSuppressedAlerts: StrictBool | None = None
