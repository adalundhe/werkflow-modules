from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sqs_change_message_visibility_batch_request_entry import SQSChangeMessageVisibilityBatchRequestEntry


class SQSChangeMessageVisibilityBatchRequest(BaseModel):
    QueueUrl: StrictStr
    Entries: list[SQSChangeMessageVisibilityBatchRequestEntry]
