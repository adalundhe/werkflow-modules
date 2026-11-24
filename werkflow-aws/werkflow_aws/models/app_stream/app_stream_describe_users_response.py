from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_user import AppStreamUser


class AppStreamDescribeUsersResponse(BaseModel):
    Users: list[AppStreamUser] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
