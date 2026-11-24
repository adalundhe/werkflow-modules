from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_behavior_model_training_summary import IoTBehaviorModelTrainingSummary


class IoTGetBehaviorModelTrainingSummariesResponse(BaseModel):
    summaries: list[IoTBehaviorModelTrainingSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
