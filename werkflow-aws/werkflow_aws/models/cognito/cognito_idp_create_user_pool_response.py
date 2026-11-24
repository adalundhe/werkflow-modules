from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_user_pool_type import CognitoIDPUserPoolType


class CognitoIDPCreateUserPoolResponse(BaseModel):
    UserPool: CognitoIDPUserPoolType | None = None
    ResponseMetadata: dict[str, Any] | None = None
