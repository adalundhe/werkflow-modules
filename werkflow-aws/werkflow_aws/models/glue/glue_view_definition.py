from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .glue_sub_object_statistics import GlueSubObjectStatistics
from .glue_view_representation import GlueViewRepresentation


class GlueViewDefinition(BaseModel):
    IsProtected: StrictBool | None = None
    IsManaged: StrictBool | None = None
    Definer: StrictStr | None = None
    ViewVersionId: StrictInt | None = None
    ViewVersionToken: StrictStr | None = None
    RefreshSeconds: StrictInt | None = None
    LastRefreshType: StrictStr | None = None
    SubObjects: list[StrictStr] | None = None
    SubObjectVersionIds: list[StrictInt] | None = None
    SubObjectsStatistics: list[GlueSubObjectStatistics] | None = None
    Representations: list[GlueViewRepresentation] | None = None
    SparkPipelineInfo: dict[StrictStr, StrictStr] | None = None
