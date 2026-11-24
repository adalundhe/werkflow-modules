from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_entity_types_evaluation_metrics import ComprehendEntityTypesEvaluationMetrics


class ComprehendEntityRecognizerMetadataEntityTypesListItem(BaseModel):
    Type: StrictStr | None = None
    EvaluationMetrics: ComprehendEntityTypesEvaluationMetrics | None = None
    NumberOfTrainMentions: StrictInt | None = None
