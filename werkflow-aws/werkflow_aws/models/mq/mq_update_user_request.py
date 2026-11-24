from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MQUpdateUserRequest(BaseModel):
    BrokerId: StrictStr
    Username: StrictStr
    ConsoleAccess: StrictBool | None = None
    Groups: list[StrictStr] | None = None
    Password: StrictStr | None = None
    ReplicationUser: StrictBool | None = None
