from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSListSubscriptionsByTopicRequest(BaseModel):
    TopicArn: StrictStr
    NextToken: StrictStr | None = None
