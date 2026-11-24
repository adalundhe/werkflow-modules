from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_user_type import CognitoIDPUserType


class CognitoIDPListUsersInGroupResponse(BaseModel):
    Users: list[CognitoIDPUserType] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
