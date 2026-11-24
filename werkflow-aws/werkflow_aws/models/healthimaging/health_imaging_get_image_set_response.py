from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .health_imaging_overrides import HealthImagingOverrides


class HealthImagingGetImageSetResponse(BaseModel):
    datastoreId: StrictStr | None = None
    imageSetId: StrictStr | None = None
    versionId: StrictStr | None = None
    imageSetState: StrictStr | None = None
    imageSetWorkflowStatus: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    deletedAt: datetime.datetime | StrictStr | None = None
    message: StrictStr | None = None
    imageSetArn: StrictStr | None = None
    overrides: HealthImagingOverrides | None = None
    isPrimary: StrictBool | None = None
    lastAccessedAt: datetime.datetime | StrictStr | None = None
    storageTier: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
