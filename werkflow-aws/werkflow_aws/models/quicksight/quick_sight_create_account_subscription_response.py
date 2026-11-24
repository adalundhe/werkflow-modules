from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_signup_response import QuickSightSignupResponse


class QuickSightCreateAccountSubscriptionResponse(BaseModel):
    SignupResponse: QuickSightSignupResponse | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
