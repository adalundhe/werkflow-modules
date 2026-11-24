from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsSqsQueueDetails(BaseModel):
    KmsDataKeyReusePeriodSeconds: StrictInt | None = None
    KmsMasterKeyId: StrictStr | None = None
    QueueName: StrictStr | None = None
    DeadLetterTargetArn: StrictStr | None = None
