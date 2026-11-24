from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_trail_import_source import CloudTrailImportSource


class CloudTrailStartImportRequest(BaseModel):
    Destinations: list[StrictStr] | None = None
    ImportSource: CloudTrailImportSource | None = None
    StartEventTime: datetime.datetime | StrictStr | None = None
    EndEventTime: datetime.datetime | StrictStr | None = None
    ImportId: StrictStr | None = None
