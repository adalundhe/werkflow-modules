from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_event_tracker_summary import PersonalizeEventTrackerSummary


class PersonalizeListEventTrackersResponse(BaseModel):
    eventTrackers: list[PersonalizeEventTrackerSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
