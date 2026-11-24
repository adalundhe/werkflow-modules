from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CognitoIDPUpdateAuthEventFeedbackRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    EventId: StrictStr
    FeedbackToken: StrictStr
    FeedbackValue: Literal['Valid', 'Invalid']
