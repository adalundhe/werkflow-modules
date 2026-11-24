from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_failure_description import FirehoseFailureDescription


class FirehoseDeliveryStreamEncryptionConfiguration(BaseModel):
    KeyARN: StrictStr | None = None
    KeyType: StrictStr | None = None
    Status: StrictStr | None = None
    FailureDescription: FirehoseFailureDescription | None = None
