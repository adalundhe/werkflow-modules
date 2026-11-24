from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoSyncDataset(BaseModel):
    IdentityId: StrictStr | None = None
    DatasetName: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
    LastModifiedBy: StrictStr | None = None
    DataStorage: StrictInt | None = None
    NumRecords: StrictInt | None = None
