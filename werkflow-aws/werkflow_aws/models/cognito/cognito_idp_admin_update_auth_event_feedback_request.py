from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CognitoIDPAdminUpdateAuthEventFeedbackRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    EventId: StrictStr
    FeedbackValue: Literal['Valid', 'Invalid']
