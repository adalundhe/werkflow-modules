from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_entity_recognizer_properties import ComprehendEntityRecognizerProperties


class ComprehendDescribeEntityRecognizerResponse(BaseModel):
    EntityRecognizerProperties: ComprehendEntityRecognizerProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
