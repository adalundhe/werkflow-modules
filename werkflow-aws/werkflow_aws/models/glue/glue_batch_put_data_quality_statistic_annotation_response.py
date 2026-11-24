from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_annotation_error import GlueAnnotationError


class GlueBatchPutDataQualityStatisticAnnotationResponse(BaseModel):
    FailedInclusionAnnotations: list[GlueAnnotationError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
