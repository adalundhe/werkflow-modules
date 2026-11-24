from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .firehose_retry_options import FirehoseRetryOptions


class FirehoseDynamicPartitioningConfiguration(BaseModel):
    RetryOptions: FirehoseRetryOptions | None = None
    Enabled: StrictBool | None = None
