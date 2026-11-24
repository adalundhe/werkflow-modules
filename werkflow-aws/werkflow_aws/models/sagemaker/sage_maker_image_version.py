from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerImageVersion(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    ImageArn: StrictStr | None = None
    ImageVersionArn: StrictStr | None = None
    ImageVersionStatus: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    Version: StrictInt | None = None
