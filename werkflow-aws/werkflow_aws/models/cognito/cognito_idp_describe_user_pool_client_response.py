from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_user_pool_client_type import CognitoIDPUserPoolClientType


class CognitoIDPDescribeUserPoolClientResponse(BaseModel):
    UserPoolClient: CognitoIDPUserPoolClientType | None = None
    ResponseMetadata: dict[str, Any] | None = None
