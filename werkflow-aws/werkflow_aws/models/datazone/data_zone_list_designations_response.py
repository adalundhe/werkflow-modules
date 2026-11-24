from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_designation_summary import DataZoneDesignationSummary


class DataZoneListDesignationsResponse(BaseModel):
    items: list[DataZoneDesignationSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
