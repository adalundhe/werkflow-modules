from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_key_values_pair import BatchKeyValuesPair


class BatchListServiceJobsRequest(BaseModel):
    jobQueue: StrictStr | None = None
    jobStatus: Literal['SUBMITTED', 'PENDING', 'RUNNABLE', 'SCHEDULED', 'STARTING', 'RUNNING', 'SUCCEEDED', 'FAILED'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    filters: list[BatchKeyValuesPair] | None = None
