from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class DataZoneStartNotebookExportResponse(BaseModel):
    id: StrictStr | None = None
    domainId: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    notebookId: StrictStr | None = None
    fileFormat: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
