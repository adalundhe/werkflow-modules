from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MQUser(BaseModel):
    Password: StrictStr
    Username: StrictStr
    ConsoleAccess: StrictBool | None = None
    Groups: list[StrictStr] | None = None
    ReplicationUser: StrictBool | None = None
