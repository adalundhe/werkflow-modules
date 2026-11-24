from __future__ import annotations
from pydantic import BaseModel
from .sqs_batch_result_error_entry import SQSBatchResultErrorEntry
from .sqs_change_message_visibility_batch_result_entry import SQSChangeMessageVisibilityBatchResultEntry


class SQSChangeMessageVisibilityBatchResponse(BaseModel):
    Successful: list[SQSChangeMessageVisibilityBatchResultEntry] | None = None
    Failed: list[SQSBatchResultErrorEntry] | None = None
