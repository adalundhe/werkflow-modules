from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ses_topic_preference import SESTopicPreference


class SESCreateContactRequest(BaseModel):
    ContactListName: StrictStr
    EmailAddress: StrictStr
    TopicPreferences: list[SESTopicPreference] | None = None
    UnsubscribeAll: StrictBool | None = None
    AttributesData: StrictStr | None = None
