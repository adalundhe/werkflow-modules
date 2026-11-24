from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_entity_recognizer_filter import ComprehendEntityRecognizerFilter


class ComprehendListEntityRecognizersRequest(BaseModel):
    Filter: ComprehendEntityRecognizerFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
