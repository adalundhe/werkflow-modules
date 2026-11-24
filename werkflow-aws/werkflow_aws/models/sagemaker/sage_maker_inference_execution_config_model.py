from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerInferenceExecutionConfigModel(BaseModel):
    Mode: StrictStr | None = None
