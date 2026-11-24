from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingPutMessageFeedbackRequest(BaseModel):
    MessageId: StrictStr
    MessageFeedbackStatus: Literal['RECEIVED', 'FAILED']
