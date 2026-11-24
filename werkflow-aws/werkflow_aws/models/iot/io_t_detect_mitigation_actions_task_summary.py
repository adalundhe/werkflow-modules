from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_detect_mitigation_actions_task_statistics import IoTDetectMitigationActionsTaskStatistics
from .io_t_detect_mitigation_actions_task_target import IoTDetectMitigationActionsTaskTarget
from .io_t_mitigation_action import IoTMitigationAction
from .io_t_violation_event_occurrence_range import IoTViolationEventOccurrenceRange


class IoTDetectMitigationActionsTaskSummary(BaseModel):
    taskId: StrictStr | None = None
    taskStatus: StrictStr | None = None
    taskStartTime: datetime.datetime | StrictStr | None = None
    taskEndTime: datetime.datetime | StrictStr | None = None
    target: IoTDetectMitigationActionsTaskTarget | None = None
    violationEventOccurrenceRange: IoTViolationEventOccurrenceRange | None = None
    onlyActiveViolationsIncluded: StrictBool | None = None
    suppressedAlertsIncluded: StrictBool | None = None
    actionsDefinition: list[IoTMitigationAction] | None = None
    taskStatistics: IoTDetectMitigationActionsTaskStatistics | None = None
