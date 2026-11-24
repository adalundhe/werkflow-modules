from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dimension_value_attribute import DimensionValueAttribute


class CostExplorerGetDimensionValuesResponse(BaseModel):
    DimensionValues: list[DimensionValueAttribute] | None = None
    ReturnSize: StrictInt | None = None
    TotalSize: StrictInt | None = None
    NextPageToken: StrictStr | None = None
