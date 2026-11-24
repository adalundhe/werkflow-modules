from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .sns_batch_result_error_entry import SNSBatchResultErrorEntry
from .sns_publish_batch_result_entry import SNSPublishBatchResultEntry


class SNSPublishBatchResponse(BaseModel):
    Successful: list[SNSPublishBatchResultEntry] | None = None
    Failed: list[SNSBatchResultErrorEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
