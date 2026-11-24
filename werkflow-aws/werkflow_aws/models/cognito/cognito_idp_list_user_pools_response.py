from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_user_pool_description_type import CognitoIDPUserPoolDescriptionType


class CognitoIDPListUserPoolsResponse(BaseModel):
    UserPools: list[CognitoIDPUserPoolDescriptionType] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
