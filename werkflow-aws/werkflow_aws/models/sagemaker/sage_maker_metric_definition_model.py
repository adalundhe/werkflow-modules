from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerMetricDefinitionModel(BaseModel):
    Name: StrictStr | None = None
    Regex: StrictStr | None = None
