from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_session_description_type import CognitoIDPSessionDescriptionType


class CognitoIDPListUserSessionsResponse(BaseModel):
    Sessions: list[CognitoIDPSessionDescriptionType] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
