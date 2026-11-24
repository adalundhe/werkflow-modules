from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCreateTrainingJobResponse(BaseModel):
    TrainingJobArn: StrictStr | None = None
