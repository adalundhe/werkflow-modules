from __future__ import annotations
from pydantic import BaseModel
from .personalize_event_parameters import PersonalizeEventParameters


class PersonalizeEventsConfig(BaseModel):
    eventParametersList: list[PersonalizeEventParameters] | None = None
