from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_entity_recognizer_properties import ComprehendEntityRecognizerProperties


class ComprehendListEntityRecognizersResponse(BaseModel):
    EntityRecognizerPropertiesList: list[ComprehendEntityRecognizerProperties] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
