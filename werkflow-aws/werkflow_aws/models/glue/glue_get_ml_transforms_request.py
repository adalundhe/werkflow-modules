from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_transform_filter_criteria import GlueTransformFilterCriteria
from .glue_transform_sort_criteria import GlueTransformSortCriteria


class GlueGetMLTransformsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Filter: GlueTransformFilterCriteria | None = None
    Sort: GlueTransformSortCriteria | None = None
