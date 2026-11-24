from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_metadata_generation_run_target import DataZoneMetadataGenerationRunTarget
from .data_zone_metadata_generation_run_type_stat import DataZoneMetadataGenerationRunTypeStat


class DataZoneGetMetadataGenerationRunResponse(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    target: DataZoneMetadataGenerationRunTarget | None = None
    status: StrictStr | None = None
    type: StrictStr | None = None
    types: list[StrictStr] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    typeStats: list[DataZoneMetadataGenerationRunTypeStat] | None = None
    ResponseMetadata: dict[str, Any] | None = None
