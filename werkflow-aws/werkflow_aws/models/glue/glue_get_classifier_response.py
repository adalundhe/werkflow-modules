from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_classifier import GlueClassifier


class GlueGetClassifierResponse(BaseModel):
    Classifier: GlueClassifier | None = None
    ResponseMetadata: dict[str, Any] | None = None
