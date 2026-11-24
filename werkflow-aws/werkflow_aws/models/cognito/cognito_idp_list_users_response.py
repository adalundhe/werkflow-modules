from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_user_type import CognitoIDPUserType


class CognitoIDPListUsersResponse(BaseModel):
    Users: list[CognitoIDPUserType] | None = None
    PaginationToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
