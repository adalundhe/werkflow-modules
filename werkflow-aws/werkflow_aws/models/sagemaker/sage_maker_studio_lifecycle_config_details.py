from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerStudioLifecycleConfigDetails(BaseModel):
    StudioLifecycleConfigArn: StrictStr | None = None
    StudioLifecycleConfigName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    StudioLifecycleConfigAppType: StrictStr | None = None
