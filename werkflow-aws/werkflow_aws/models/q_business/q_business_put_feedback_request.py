from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .q_business_message_usefulness_feedback import QBusinessMessageUsefulnessFeedback


class QBusinessPutFeedbackRequest(BaseModel):
    applicationId: StrictStr
    conversationId: StrictStr
    messageId: StrictStr
    userId: StrictStr | None = None
    messageCopiedAt: datetime.datetime | StrictStr | None = None
    messageUsefulness: QBusinessMessageUsefulnessFeedback | None = None
