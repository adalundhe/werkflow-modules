from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_import_source import CloudTrailImportSource
from .cloud_trail_import_statistics import CloudTrailImportStatistics


class CloudTrailStopImportResponse(BaseModel):
    ImportId: StrictStr | None = None
    ImportSource: CloudTrailImportSource | None = None
    Destinations: list[StrictStr] | None = None
    ImportStatus: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    UpdatedTimestamp: datetime.datetime | StrictStr | None = None
    StartEventTime: datetime.datetime | StrictStr | None = None
    EndEventTime: datetime.datetime | StrictStr | None = None
    ImportStatistics: CloudTrailImportStatistics | None = None
    ResponseMetadata: dict[str, Any] | None = None
