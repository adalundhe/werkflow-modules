from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sqs_delete_message_batch_request_entry import SQSDeleteMessageBatchRequestEntry


class SQSDeleteMessageBatchRequest(BaseModel):
    QueueUrl: StrictStr
    Entries: list[SQSDeleteMessageBatchRequestEntry]
