from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_datapoint_inclusion_annotation import GlueDatapointInclusionAnnotation


class GlueBatchPutDataQualityStatisticAnnotationRequest(BaseModel):
    InclusionAnnotations: list[GlueDatapointInclusionAnnotation]
    ClientToken: StrictStr | None = None
