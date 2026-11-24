from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerBatchDescribeModelPackageError(BaseModel):
    ErrorCode: StrictStr | None = None
    ErrorResponse: StrictStr | None = None
