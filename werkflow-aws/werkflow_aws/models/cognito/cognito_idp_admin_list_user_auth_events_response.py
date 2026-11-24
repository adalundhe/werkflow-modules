from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_auth_event_type import CognitoIDPAuthEventType


class CognitoIDPAdminListUserAuthEventsResponse(BaseModel):
    AuthEvents: list[CognitoIDPAuthEventType] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
