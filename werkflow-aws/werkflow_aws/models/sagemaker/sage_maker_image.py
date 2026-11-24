from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerImage(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    FailureReason: StrictStr | None = None
    ImageArn: StrictStr | None = None
    ImageName: StrictStr | None = None
    ImageStatus: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
