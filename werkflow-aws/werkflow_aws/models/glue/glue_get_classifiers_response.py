from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_classifier import GlueClassifier


class GlueGetClassifiersResponse(BaseModel):
    Classifiers: list[GlueClassifier] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
