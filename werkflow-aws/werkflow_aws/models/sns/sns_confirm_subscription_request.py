from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSConfirmSubscriptionRequest(BaseModel):
    TopicArn: StrictStr
    Token: StrictStr
    AuthenticateOnUnsubscribe: StrictStr | None = None
