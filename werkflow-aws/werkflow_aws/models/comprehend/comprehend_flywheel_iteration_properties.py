from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .comprehend_flywheel_model_evaluation_metrics import ComprehendFlywheelModelEvaluationMetrics


class ComprehendFlywheelIterationProperties(BaseModel):
    FlywheelArn: StrictStr | None = None
    FlywheelIterationId: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    Message: StrictStr | None = None
    EvaluatedModelArn: StrictStr | None = None
    EvaluatedModelMetrics: ComprehendFlywheelModelEvaluationMetrics | None = None
    TrainedModelArn: StrictStr | None = None
    TrainedModelMetrics: ComprehendFlywheelModelEvaluationMetrics | None = None
    EvaluationManifestS3Prefix: StrictStr | None = None
