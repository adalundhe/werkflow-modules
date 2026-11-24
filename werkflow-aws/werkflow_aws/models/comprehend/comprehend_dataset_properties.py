from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ComprehendDatasetProperties(BaseModel):
    DatasetArn: StrictStr | None = None
    DatasetName: StrictStr | None = None
    DatasetType: StrictStr | None = None
    DatasetS3Uri: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    Message: StrictStr | None = None
    NumberOfDocuments: StrictInt | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
