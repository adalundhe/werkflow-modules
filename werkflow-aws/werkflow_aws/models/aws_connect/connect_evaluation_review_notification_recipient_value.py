from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEvaluationReviewNotificationRecipientValue(BaseModel):
    UserId: StrictStr | None = None
