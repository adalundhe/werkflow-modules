from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_training_session_summary import SageMakerTrainingSessionSummary


class SageMakerListTrainingSessionsResponse(BaseModel):
    NextToken: StrictStr | None = None
    TrainingSessionSummaries: list[SageMakerTrainingSessionSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
