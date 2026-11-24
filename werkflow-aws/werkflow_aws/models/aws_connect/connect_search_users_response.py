from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_user_search_summary import ConnectUserSearchSummary


class ConnectSearchUsersResponse(BaseModel):
    Users: list[ConnectUserSearchSummary] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
