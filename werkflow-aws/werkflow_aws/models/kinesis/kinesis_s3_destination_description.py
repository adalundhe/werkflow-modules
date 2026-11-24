from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .kinesis_dead_letter_queue_s3_configuration import KinesisDeadLetterQueueS3Configuration
from .kinesis_s3_storage_configuration import KinesisS3StorageConfiguration


class KinesisS3DestinationDescription(BaseModel):
    DataFreshnessInSeconds: StrictInt | None = None
    DeadLetterQueueS3Configuration: KinesisDeadLetterQueueS3Configuration | None = None
    StorageConfiguration: KinesisS3StorageConfiguration | None = None
