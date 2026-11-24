from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .health_imaging_overrides import HealthImagingOverrides


class HealthImagingImageSetProperties(BaseModel):
    imageSetId: StrictStr | None = None
    versionId: StrictStr | None = None
    imageSetState: StrictStr | None = None
    ImageSetWorkflowStatus: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    deletedAt: datetime.datetime | StrictStr | None = None
    message: StrictStr | None = None
    overrides: HealthImagingOverrides | None = None
    isPrimary: StrictBool | None = None
