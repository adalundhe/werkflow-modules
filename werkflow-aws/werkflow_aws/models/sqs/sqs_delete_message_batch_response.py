from __future__ import annotations
from pydantic import BaseModel
from .sqs_batch_result_error_entry import SQSBatchResultErrorEntry
from .sqs_delete_message_batch_result_entry import SQSDeleteMessageBatchResultEntry


class SQSDeleteMessageBatchResponse(BaseModel):
    Successful: list[SQSDeleteMessageBatchResultEntry] | None = None
    Failed: list[SQSBatchResultErrorEntry] | None = None
