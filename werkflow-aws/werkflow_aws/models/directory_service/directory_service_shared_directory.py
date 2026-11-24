from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DirectoryServiceSharedDirectory(BaseModel):
    OwnerAccountId: StrictStr | None = None
    OwnerDirectoryId: StrictStr | None = None
    ShareMethod: StrictStr | None = None
    SharedAccountId: StrictStr | None = None
    SharedDirectoryId: StrictStr | None = None
    ShareStatus: StrictStr | None = None
    ShareNotes: StrictStr | None = None
    CreatedDateTime: datetime.datetime | StrictStr | None = None
    LastUpdatedDateTime: datetime.datetime | StrictStr | None = None
