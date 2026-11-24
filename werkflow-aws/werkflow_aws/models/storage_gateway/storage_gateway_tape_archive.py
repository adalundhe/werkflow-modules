from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class StorageGatewayTapeArchive(BaseModel):
    TapeARN: StrictStr | None = None
    TapeBarcode: StrictStr | None = None
    TapeCreatedDate: datetime.datetime | StrictStr | None = None
    TapeSizeInBytes: StrictInt | None = None
    CompletionTime: datetime.datetime | StrictStr | None = None
    RetrievedTo: StrictStr | None = None
    TapeStatus: StrictStr | None = None
    TapeUsedInBytes: StrictInt | None = None
    KMSKey: StrictStr | None = None
    PoolId: StrictStr | None = None
    Worm: StrictBool | None = None
    RetentionStartDate: datetime.datetime | StrictStr | None = None
    PoolEntryDate: datetime.datetime | StrictStr | None = None
