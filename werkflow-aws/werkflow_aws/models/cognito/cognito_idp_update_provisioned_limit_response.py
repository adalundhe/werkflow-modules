from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_limit_type import CognitoIDPLimitType


class CognitoIDPUpdateProvisionedLimitResponse(BaseModel):
    Limit: CognitoIDPLimitType | None = None
    ResponseMetadata: dict[str, Any] | None = None
