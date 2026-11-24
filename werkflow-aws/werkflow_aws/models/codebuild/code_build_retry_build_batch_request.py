from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeBuildRetryBuildBatchRequest(BaseModel):
    id: StrictStr | None = None
    idempotencyToken: StrictStr | None = None
    retryType: Literal['RETRY_ALL_BUILDS', 'RETRY_FAILED_BUILDS'] | None = None
