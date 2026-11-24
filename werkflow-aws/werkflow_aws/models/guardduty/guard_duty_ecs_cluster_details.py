from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_ecs_task_details import GuardDutyEcsTaskDetails
from .guard_duty_tag import GuardDutyTag


class GuardDutyEcsClusterDetails(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    Status: StrictStr | None = None
    ActiveServicesCount: StrictInt | None = None
    RegisteredContainerInstancesCount: StrictInt | None = None
    RunningTasksCount: StrictInt | None = None
    Tags: list[GuardDutyTag] | None = None
    TaskDetails: GuardDutyEcsTaskDetails | None = None
