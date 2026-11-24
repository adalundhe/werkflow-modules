from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .ses_topic_preference import SESTopicPreference


class SESContact(BaseModel):
    EmailAddress: StrictStr | None = None
    TopicPreferences: list[SESTopicPreference] | None = None
    TopicDefaultPreferences: list[SESTopicPreference] | None = None
    UnsubscribeAll: StrictBool | None = None
    LastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
