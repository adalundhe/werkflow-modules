from __future__ import annotations
from pydantic import BaseModel
from .sqs_batch_result_error_entry import SQSBatchResultErrorEntry
from .sqs_send_message_batch_result_entry import SQSSendMessageBatchResultEntry


class SQSSendMessageBatchResponse(BaseModel):
    Successful: list[SQSSendMessageBatchResultEntry] | None = None
    Failed: list[SQSBatchResultErrorEntry] | None = None
