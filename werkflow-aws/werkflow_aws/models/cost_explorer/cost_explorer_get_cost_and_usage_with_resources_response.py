from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cost_explorer_dimension_values_with_attributes import CostExplorerDimensionValuesWithAttributes
from .cost_explorer_group_definition import CostExplorerGroupDefinition
from .cost_explorer_result_by_time import CostExplorerResultByTime


class CostExplorerGetCostAndUsageWithResourcesResponse(BaseModel):
    NextPageToken: StrictStr | None = None
    GroupDefinitions: list[CostExplorerGroupDefinition] | None = None
    ResultsByTime: list[CostExplorerResultByTime] | None = None
    DimensionValueAttributes: list[CostExplorerDimensionValuesWithAttributes] | None = None
    ResponseMetadata: dict[str, Any] | None = None
