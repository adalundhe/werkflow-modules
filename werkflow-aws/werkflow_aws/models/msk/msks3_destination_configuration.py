from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .msk_dead_letter_queue_s3 import MSKDeadLetterQueueS3
from .msks3_storage import MSKS3Storage


class MSKS3DestinationConfiguration(BaseModel):
    DataFreshnessInSeconds: StrictInt | None = None
    DeadLetterQueueS3: MSKDeadLetterQueueS3 | None = None
    ServiceExecutionRoleArn: StrictStr | None = None
    Storage: MSKS3Storage | None = None
