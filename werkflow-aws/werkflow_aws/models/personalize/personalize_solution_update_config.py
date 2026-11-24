from __future__ import annotations
from pydantic import BaseModel
from .personalize_auto_training_config import PersonalizeAutoTrainingConfig
from .personalize_events_config import PersonalizeEventsConfig


class PersonalizeSolutionUpdateConfig(BaseModel):
    autoTrainingConfig: PersonalizeAutoTrainingConfig | None = None
    eventsConfig: PersonalizeEventsConfig | None = None
