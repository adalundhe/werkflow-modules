from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sqs_send_message_batch_request_entry import SQSSendMessageBatchRequestEntry


class SQSSendMessageBatchRequest(BaseModel):
    QueueUrl: StrictStr
    Entries: list[SQSSendMessageBatchRequestEntry]
