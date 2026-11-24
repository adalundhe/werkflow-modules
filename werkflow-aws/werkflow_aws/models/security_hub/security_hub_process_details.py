from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubProcessDetails(BaseModel):
    Name: StrictStr | None = None
    Path: StrictStr | None = None
    Pid: StrictInt | None = None
    ParentPid: StrictInt | None = None
    LaunchedAt: StrictStr | None = None
    TerminatedAt: StrictStr | None = None
