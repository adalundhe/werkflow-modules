from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_failed_key_registration_entry import QuickSightFailedKeyRegistrationEntry
from .quick_sight_successful_key_registration_entry import QuickSightSuccessfulKeyRegistrationEntry


class QuickSightUpdateKeyRegistrationResponse(BaseModel):
    FailedKeyRegistration: list[QuickSightFailedKeyRegistrationEntry] | None = None
    SuccessfulKeyRegistration: list[QuickSightSuccessfulKeyRegistrationEntry] | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
