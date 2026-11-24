from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerMlflowAppSummary(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    MlflowVersion: StrictStr | None = None
