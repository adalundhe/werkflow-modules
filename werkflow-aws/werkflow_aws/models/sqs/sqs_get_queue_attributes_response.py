from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sqs_queue_attribute_name import SQSQueueAttributeName


class SQSGetQueueAttributesResponse(BaseModel):
    Attributes: dict[SQSQueueAttributeName, StrictStr] | None = None
