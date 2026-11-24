from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_metadata_generation_run_item import DataZoneMetadataGenerationRunItem


class DataZoneListMetadataGenerationRunsResponse(BaseModel):
    items: list[DataZoneMetadataGenerationRunItem] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
