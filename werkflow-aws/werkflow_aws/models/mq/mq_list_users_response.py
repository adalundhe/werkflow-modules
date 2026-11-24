from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .mq_user_summary import MQUserSummary


class MQListUsersResponse(BaseModel):
    BrokerId: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Users: list[MQUserSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
