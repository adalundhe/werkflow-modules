from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_user_data import ConnectUserData


class ConnectGetCurrentUserDataResponse(BaseModel):
    NextToken: StrictStr | None = None
    UserDataList: list[ConnectUserData] | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
