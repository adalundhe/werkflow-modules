from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class RekognitionDatasetMetadata(BaseModel):
    CreationTimestamp: datetime.datetime | StrictStr | None = None
    DatasetType: StrictStr | None = None
    DatasetArn: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    StatusMessageCode: StrictStr | None = None
