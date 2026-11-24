from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sqs_message_attribute_value import SQSMessageAttributeValue
from .sqs_message_system_attribute_name_for_sends import SQSMessageSystemAttributeNameForSends
from .sqs_message_system_attribute_value import SQSMessageSystemAttributeValue


class SQSSendMessageBatchRequestEntry(BaseModel):
    Id: StrictStr
    MessageBody: StrictStr
    DelaySeconds: StrictInt | None = None
    MessageAttributes: dict[StrictStr, SQSMessageAttributeValue] | None = None
    MessageSystemAttributes: dict[SQSMessageSystemAttributeNameForSends, SQSMessageSystemAttributeValue] | None = None
    MessageDeduplicationId: StrictStr | None = None
    MessageGroupId: StrictStr | None = None
