from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .kinesis_dead_letter_configuration import KinesisDeadLetterConfiguration


class KinesisQueueAttributes(BaseModel):
    VisibilityTimeoutSeconds: StrictInt | None = None
    DeadLetterConfiguration: KinesisDeadLetterConfiguration | None = None
