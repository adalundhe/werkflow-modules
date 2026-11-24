from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cloud_watch_tag_model import CloudWatchTagModel


class CloudWatchPutMetricDataQueryDefinitionRequest(BaseModel):
    Path: StrictStr
    Expression: StrictStr
    Type: Literal['PROMQL', 'SQL', 'METRIC_MATH']
    Id: StrictStr | None = None
    Tags: list[CloudWatchTagModel] | None = None
