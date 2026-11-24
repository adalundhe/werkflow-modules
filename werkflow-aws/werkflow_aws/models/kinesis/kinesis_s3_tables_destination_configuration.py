from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .kinesis_dead_letter_queue_s3_configuration import KinesisDeadLetterQueueS3Configuration
from .kinesis_s3_tables_configuration import KinesisS3TablesConfiguration


class KinesisS3TablesDestinationConfiguration(BaseModel):
    DeadLetterQueueS3Configuration: KinesisDeadLetterQueueS3Configuration
    S3TablesConfigurationList: list[KinesisS3TablesConfiguration]
    DataFreshnessInSeconds: StrictInt | None = None
