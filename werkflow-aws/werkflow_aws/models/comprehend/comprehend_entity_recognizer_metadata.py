from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .comprehend_entity_recognizer_evaluation_metrics import ComprehendEntityRecognizerEvaluationMetrics
from .comprehend_entity_recognizer_metadata_entity_types_list_item import ComprehendEntityRecognizerMetadataEntityTypesListItem


class ComprehendEntityRecognizerMetadata(BaseModel):
    NumberOfTrainedDocuments: StrictInt | None = None
    NumberOfTestDocuments: StrictInt | None = None
    EvaluationMetrics: ComprehendEntityRecognizerEvaluationMetrics | None = None
    EntityTypes: list[ComprehendEntityRecognizerMetadataEntityTypesListItem] | None = None
