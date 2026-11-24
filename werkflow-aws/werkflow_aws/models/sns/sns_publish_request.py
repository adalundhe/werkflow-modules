from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sns_message_attribute_value import SNSMessageAttributeValue


class SNSPublishRequest(BaseModel):
    Message: StrictStr
    TopicArn: StrictStr | None = None
    TargetArn: StrictStr | None = None
    PhoneNumber: StrictStr | None = None
    Subject: StrictStr | None = None
    MessageStructure: StrictStr | None = None
    MessageAttributes: dict[StrictStr, SNSMessageAttributeValue] | None = None
    MessageDeduplicationId: StrictStr | None = None
    MessageGroupId: StrictStr | None = None
