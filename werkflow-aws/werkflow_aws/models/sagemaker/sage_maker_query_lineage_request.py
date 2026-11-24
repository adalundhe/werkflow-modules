from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .sage_maker_query_filters import SageMakerQueryFilters


class SageMakerQueryLineageRequest(BaseModel):
    StartArns: list[StrictStr] | None = None
    Direction: Literal['Both', 'Ascendants', 'Descendants'] | None = None
    IncludeEdges: StrictBool | None = None
    Filters: SageMakerQueryFilters | None = None
    MaxDepth: StrictInt | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
