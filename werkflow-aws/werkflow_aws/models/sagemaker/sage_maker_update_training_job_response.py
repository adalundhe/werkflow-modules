from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerUpdateTrainingJobResponse(BaseModel):
    TrainingJobArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
