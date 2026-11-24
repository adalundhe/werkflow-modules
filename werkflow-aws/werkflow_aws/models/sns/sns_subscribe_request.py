from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SNSSubscribeRequest(BaseModel):
    TopicArn: StrictStr
    Protocol: StrictStr
    Endpoint: StrictStr | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
    ReturnSubscriptionArn: StrictBool | None = None
