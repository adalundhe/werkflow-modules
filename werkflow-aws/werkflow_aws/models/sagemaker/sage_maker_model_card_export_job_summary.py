from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerModelCardExportJobSummary(BaseModel):
    ModelCardExportJobName: StrictStr | None = None
    ModelCardExportJobArn: StrictStr | None = None
    Status: StrictStr | None = None
    ModelCardName: StrictStr | None = None
    ModelCardVersion: StrictInt | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    LastModifiedAt: datetime.datetime | StrictStr | None = None
