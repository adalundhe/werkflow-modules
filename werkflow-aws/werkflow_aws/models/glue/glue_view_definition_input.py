from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .glue_sub_object_statistics import GlueSubObjectStatistics
from .glue_view_representation_input import GlueViewRepresentationInput


class GlueViewDefinitionInput(BaseModel):
    IsProtected: StrictBool | None = None
    IsManaged: StrictBool | None = None
    Definer: StrictStr | None = None
    Representations: list[GlueViewRepresentationInput] | None = None
    ViewVersionId: StrictInt | None = None
    ViewVersionToken: StrictStr | None = None
    RefreshSeconds: StrictInt | None = None
    LastRefreshType: Literal['FULL', 'INCREMENTAL'] | None = None
    SubObjects: list[StrictStr] | None = None
    SubObjectVersionIds: list[StrictInt] | None = None
    SubObjectsStatistics: list[GlueSubObjectStatistics] | None = None
    SparkPipelineInfo: dict[StrictStr, StrictStr] | None = None
