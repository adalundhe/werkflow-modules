from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sqs_queue_attribute_name import SQSQueueAttributeName


class SQSCreateQueueRequest(BaseModel):
    QueueName: StrictStr
    Attributes: dict[SQSQueueAttributeName, StrictStr] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
