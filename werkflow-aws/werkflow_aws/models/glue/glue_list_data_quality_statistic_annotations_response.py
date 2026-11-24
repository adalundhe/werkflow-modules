from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_statistic_annotation import GlueStatisticAnnotation


class GlueListDataQualityStatisticAnnotationsResponse(BaseModel):
    Annotations: list[GlueStatisticAnnotation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
