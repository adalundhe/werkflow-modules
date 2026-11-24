from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerJobConfigSchemaVersionSummary(BaseModel):
    JobConfigSchemaVersion: StrictStr | None = None
