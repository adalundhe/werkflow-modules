from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_user_summary import ConnectUserSummary


class ConnectListUsersResponse(BaseModel):
    UserSummaryList: list[ConnectUserSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
