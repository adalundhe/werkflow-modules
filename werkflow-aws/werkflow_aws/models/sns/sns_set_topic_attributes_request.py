from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSSetTopicAttributesRequest(BaseModel):
    TopicArn: StrictStr
    AttributeName: StrictStr
    AttributeValue: StrictStr | None = None
