from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .comprehend_document_classification_config import ComprehendDocumentClassificationConfig
from .comprehend_entity_recognition_config import ComprehendEntityRecognitionConfig


class ComprehendTaskConfig(BaseModel):
    LanguageCode: StrictStr | None = None
    DocumentClassificationConfig: ComprehendDocumentClassificationConfig | None = None
    EntityRecognitionConfig: ComprehendEntityRecognitionConfig | None = None
