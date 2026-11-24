from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_result_item import DataZoneResultItem


class DataZoneQueryGraphResponse(BaseModel):
    items: list[DataZoneResultItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
