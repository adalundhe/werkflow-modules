from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .sage_maker_training_session_detail import SageMakerTrainingSessionDetail


class SageMakerDescribeTrainingSessionResponse(BaseModel):
    TrainingSessionDetail: SageMakerTrainingSessionDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
