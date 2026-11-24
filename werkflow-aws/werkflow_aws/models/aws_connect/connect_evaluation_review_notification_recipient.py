from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_review_notification_recipient_value import ConnectEvaluationReviewNotificationRecipientValue


class ConnectEvaluationReviewNotificationRecipient(BaseModel):
    Type: StrictStr | None = None
    Value: ConnectEvaluationReviewNotificationRecipientValue | None = None
