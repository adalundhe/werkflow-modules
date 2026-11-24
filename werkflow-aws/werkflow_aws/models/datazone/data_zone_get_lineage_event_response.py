from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class DataZoneGetLineageEventResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    domainId: StrictStr | None = None
    id: StrictStr | None = None
    event: StrictBytes | Any | None = None
    createdBy: StrictStr | None = None
    processingStatus: StrictStr | None = None
    eventTime: datetime.datetime | StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
