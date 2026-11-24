from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_metadata_generation_run_target import DataZoneMetadataGenerationRunTarget


class DataZoneMetadataGenerationRunItem(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    target: DataZoneMetadataGenerationRunTarget | None = None
    status: StrictStr | None = None
    type: StrictStr | None = None
    types: list[StrictStr] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    owningProjectId: StrictStr | None = None
