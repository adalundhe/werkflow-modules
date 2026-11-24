from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_group_type import CognitoIDPGroupType


class CognitoIDPGetGroupResponse(BaseModel):
    Group: CognitoIDPGroupType | None = None
    ResponseMetadata: dict[str, Any] | None = None
