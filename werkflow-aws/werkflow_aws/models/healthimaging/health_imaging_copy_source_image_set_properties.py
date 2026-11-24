from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class HealthImagingCopySourceImageSetProperties(BaseModel):
    imageSetId: StrictStr | None = None
    latestVersionId: StrictStr | None = None
    imageSetState: StrictStr | None = None
    imageSetWorkflowStatus: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    imageSetArn: StrictStr | None = None
