from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class HealthImagingUpdateImageSetMetadataResponse(BaseModel):
    datastoreId: StrictStr | None = None
    imageSetId: StrictStr | None = None
    latestVersionId: StrictStr | None = None
    imageSetState: StrictStr | None = None
    imageSetWorkflowStatus: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    message: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
