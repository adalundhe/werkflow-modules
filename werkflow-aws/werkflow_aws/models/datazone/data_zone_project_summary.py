from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_project_deletion_error import DataZoneProjectDeletionError


class DataZoneProjectSummary(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    projectStatus: StrictStr | None = None
    failureReasons: list[DataZoneProjectDeletionError] | None = None
    createdBy: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    domainUnitId: StrictStr | None = None
    projectCategory: StrictStr | None = None
