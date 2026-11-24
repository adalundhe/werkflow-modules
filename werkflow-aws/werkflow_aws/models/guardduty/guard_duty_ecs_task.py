from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GuardDutyEcsTask(BaseModel):
    CreatedAt: datetime.datetime | StrictStr | None = None
    TaskDefinitionArn: StrictStr | None = None
    LaunchType: StrictStr | None = None
    ContainerUids: list[StrictStr] | None = None
