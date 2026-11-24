from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_o_auth_client_application import QuickSightOAuthClientApplication


class QuickSightDescribeOAuthClientApplicationResponse(BaseModel):
    OAuthClientApplication: QuickSightOAuthClientApplication | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
