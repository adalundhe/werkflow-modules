from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2GetCapacityManagerAttributesResponse(BaseModel):
    CapacityManagerStatus: StrictStr | None = None
    OrganizationsAccess: StrictBool | None = None
    DataExportCount: StrictInt | None = None
    IngestionStatus: StrictStr | None = None
    IngestionStatusMessage: StrictStr | None = None
    EarliestDatapointTimestamp: datetime.datetime | StrictStr | None = None
    LatestDatapointTimestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
