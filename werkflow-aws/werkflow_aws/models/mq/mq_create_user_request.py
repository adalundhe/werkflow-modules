from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MQCreateUserRequest(BaseModel):
    BrokerId: StrictStr
    Password: StrictStr
    Username: StrictStr
    ConsoleAccess: StrictBool | None = None
    Groups: list[StrictStr] | None = None
    ReplicationUser: StrictBool | None = None
