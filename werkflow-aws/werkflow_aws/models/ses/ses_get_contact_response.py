from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .ses_topic_preference import SESTopicPreference


class SESGetContactResponse(BaseModel):
    ContactListName: StrictStr | None = None
    EmailAddress: StrictStr | None = None
    TopicPreferences: list[SESTopicPreference] | None = None
    TopicDefaultPreferences: list[SESTopicPreference] | None = None
    UnsubscribeAll: StrictBool | None = None
    AttributesData: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    LastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
