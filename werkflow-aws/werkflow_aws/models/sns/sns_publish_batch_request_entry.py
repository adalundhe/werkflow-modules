from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sns_message_attribute_value import SNSMessageAttributeValue


class SNSPublishBatchRequestEntry(BaseModel):
    Id: StrictStr
    Message: StrictStr
    Subject: StrictStr | None = None
    MessageStructure: StrictStr | None = None
    MessageAttributes: dict[StrictStr, SNSMessageAttributeValue] | None = None
    MessageDeduplicationId: StrictStr | None = None
    MessageGroupId: StrictStr | None = None
