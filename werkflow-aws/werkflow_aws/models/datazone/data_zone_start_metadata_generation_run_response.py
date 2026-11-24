from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class DataZoneStartMetadataGenerationRunResponse(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    status: StrictStr | None = None
    type: StrictStr | None = None
    types: list[StrictStr] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
