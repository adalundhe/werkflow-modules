from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAIBenchmarkInferenceComponent(BaseModel):
    Identifier: StrictStr | None = None
