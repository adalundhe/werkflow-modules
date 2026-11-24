from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .guard_duty_container import GuardDutyContainer
from .guard_duty_tag import GuardDutyTag
from .guard_duty_volume import GuardDutyVolume


class GuardDutyEcsTaskDetails(BaseModel):
    Arn: StrictStr | None = None
    DefinitionArn: StrictStr | None = None
    Version: StrictStr | None = None
    TaskCreatedAt: datetime.datetime | StrictStr | None = None
    StartedAt: datetime.datetime | StrictStr | None = None
    StartedBy: StrictStr | None = None
    Tags: list[GuardDutyTag] | None = None
    Volumes: list[GuardDutyVolume] | None = None
    Containers: list[GuardDutyContainer] | None = None
    Group: StrictStr | None = None
    LaunchType: StrictStr | None = None
