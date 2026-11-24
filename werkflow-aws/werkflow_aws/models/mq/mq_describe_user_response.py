from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .mq_user_pending_changes import MQUserPendingChanges


class MQDescribeUserResponse(BaseModel):
    BrokerId: StrictStr | None = None
    ConsoleAccess: StrictBool | None = None
    Groups: list[StrictStr] | None = None
    Pending: MQUserPendingChanges | None = None
    Username: StrictStr | None = None
    ReplicationUser: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
