from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_source_location import DataZoneSourceLocation


class DataZoneStartNotebookImportResponse(BaseModel):
    notebookId: StrictStr | None = None
    status: StrictStr | None = None
    domainId: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    type: StrictStr | None = None
    sourceLocation: DataZoneSourceLocation | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
