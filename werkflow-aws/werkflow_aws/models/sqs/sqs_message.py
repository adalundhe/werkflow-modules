from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sqs_message_attribute_value import SQSMessageAttributeValue
from .sqs_message_system_attribute_name import SQSMessageSystemAttributeName


class SQSMessage(BaseModel):
    MessageId: StrictStr | None = None
    ReceiptHandle: StrictStr | None = None
    MD5OfBody: StrictStr | None = None
    Body: StrictStr | None = None
    Attributes: dict[SQSMessageSystemAttributeName, StrictStr] | None = None
    MD5OfMessageAttributes: StrictStr | None = None
    MessageAttributes: dict[StrictStr, SQSMessageAttributeValue] | None = None
