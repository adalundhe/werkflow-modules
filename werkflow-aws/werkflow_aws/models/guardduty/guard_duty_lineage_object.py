from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyLineageObject(BaseModel):
    StartTime: datetime.datetime | StrictStr | None = None
    NamespacePid: StrictInt | None = None
    UserId: StrictInt | None = None
    Name: StrictStr | None = None
    Pid: StrictInt | None = None
    Uuid: StrictStr | None = None
    ExecutablePath: StrictStr | None = None
    Euid: StrictInt | None = None
    ParentUuid: StrictStr | None = None
