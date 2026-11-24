from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CognitoIDPEventFeedbackType(BaseModel):
    FeedbackValue: StrictStr | None = None
    Provider: StrictStr | None = None
    FeedbackDate: datetime.datetime | StrictStr | None = None
