from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEdgeModelSummary(BaseModel):
    ModelName: StrictStr | None = None
    ModelVersion: StrictStr | None = None
