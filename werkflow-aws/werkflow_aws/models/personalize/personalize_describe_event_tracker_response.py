from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_event_tracker import PersonalizeEventTracker


class PersonalizeDescribeEventTrackerResponse(BaseModel):
    eventTracker: PersonalizeEventTracker | None = None
    ResponseMetadata: dict[str, Any] | None = None
