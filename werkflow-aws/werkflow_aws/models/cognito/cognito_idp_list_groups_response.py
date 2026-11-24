from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_group_type import CognitoIDPGroupType


class CognitoIDPListGroupsResponse(BaseModel):
    Groups: list[CognitoIDPGroupType] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
