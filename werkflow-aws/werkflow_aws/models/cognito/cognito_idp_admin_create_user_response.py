from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_user_type import CognitoIDPUserType


class CognitoIDPAdminCreateUserResponse(BaseModel):
    User: CognitoIDPUserType | None = None
    ResponseMetadata: dict[str, Any] | None = None
