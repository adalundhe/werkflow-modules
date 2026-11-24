from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .connect_evaluation_review_notification_recipient import ConnectEvaluationReviewNotificationRecipient


class ConnectEvaluationReviewConfiguration(BaseModel):
    ReviewNotificationRecipients: list[ConnectEvaluationReviewNotificationRecipient] | None = None
    EligibilityDays: StrictInt | None = None
