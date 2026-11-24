from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAthenaStepMetadata(BaseModel):
    QueryExecutionId: StrictStr | None = None
    S3OutputLocation: StrictStr | None = None
