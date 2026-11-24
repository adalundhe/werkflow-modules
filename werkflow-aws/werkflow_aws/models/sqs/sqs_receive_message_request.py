from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sqs_message_system_attribute_name import SQSMessageSystemAttributeName
from .sqs_queue_attribute_name import SQSQueueAttributeName


class SQSReceiveMessageRequest(BaseModel):
    QueueUrl: StrictStr
    AttributeNames: list[SQSQueueAttributeName] | None = None
    MessageSystemAttributeNames: list[SQSMessageSystemAttributeName] | None = None
    MessageAttributeNames: list[StrictStr] | None = None
    MaxNumberOfMessages: StrictInt | None = None
    VisibilityTimeout: StrictInt | None = None
    WaitTimeSeconds: StrictInt | None = None
    ReceiveRequestAttemptId: StrictStr | None = None
