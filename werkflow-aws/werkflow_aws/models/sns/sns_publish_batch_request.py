from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sns_publish_batch_request_entry import SNSPublishBatchRequestEntry


class SNSPublishBatchRequest(BaseModel):
    TopicArn: StrictStr
    PublishBatchRequestEntries: list[SNSPublishBatchRequestEntry]
