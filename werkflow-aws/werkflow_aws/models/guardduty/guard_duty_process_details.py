from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_lineage_object import GuardDutyLineageObject


class GuardDutyProcessDetails(BaseModel):
    Name: StrictStr | None = None
    ExecutablePath: StrictStr | None = None
    ExecutableSha256: StrictStr | None = None
    NamespacePid: StrictInt | None = None
    Pwd: StrictStr | None = None
    Pid: StrictInt | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    Uuid: StrictStr | None = None
    ParentUuid: StrictStr | None = None
    User: StrictStr | None = None
    UserId: StrictInt | None = None
    Euid: StrictInt | None = None
    Lineage: list[GuardDutyLineageObject] | None = None
